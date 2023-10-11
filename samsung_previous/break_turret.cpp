//
//  break_turret.cpp
//  algorithm
//
//  Created by chaehee on 10/11/23.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, K, wi, wj, si, sj;
int board[10][10];
int attack[10][10];
bool up[10][10];

int dxy[][2] = {
    0,1, //우
    1,0, //하
    0,-1, //좌
    -1,0, //상
    -1,-1,
    1,1,
    -1,1,
    1,-1
};

struct Loc {
    int time, i, j;
};

struct {
    bool operator()(const Loc left, const Loc right) const {
        if (left.time == right.time) {
            if (left.i + left.j == right.i + right.j) {
                return left.j > right.j;
            }
            return left.i + left.j > right.i + right.j;
        }
        return left.time > right.time; //time이 큰 게 더 우선순위
    }
}week;

struct {
    bool operator()(const Loc left, const Loc right) const {
        if (left.time == right.time) {
            if (left.i + left.j == right.i + right.j) {
                return left.j < right.j;
            }
            return left.i + left.j < right.i + right.j;
        }
        return left.time < right.time;
    }
}strong;

void findWeeker() {
    int minCost = 1e9;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 0)
                continue;
            if (minCost > board[i][j]) {
                minCost = board[i][j];
            }
        }
    }

    vector<Loc> candidate;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (minCost == board[i][j]) {
                candidate.push_back({ attack[i][j],i,j });
            }
        }
    }

    sort(candidate.begin(), candidate.end(), week);

    wi = candidate[0].i;
    wj = candidate[0].j;

    board[wi][wj] += (N + M);
}

void findStronger() {
    int maxCost = 1; //0인 포탑은 pass
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (i == wi && j == wj)
                continue;
            if (maxCost < board[i][j]) {
                maxCost = board[i][j];
            }
        }
    }

    vector<Loc> candidate;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (i == wi && j == wj)
                continue;
            if (maxCost == board[i][j]) {
                candidate.push_back({ attack[i][j],i,j });
            }
        }
    }

    sort(candidate.begin(), candidate.end(), strong);

    si = candidate[0].i;
    sj = candidate[0].j;
}

bool laserAttack() {
    int parent[10][10][2] = { 0, };
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            for (int k = 0; k < 2; k++) {
                parent[i][j][k] = -1;
            }
        }
    }

    int visited[10][10] = { 0, };
    queue<pair<int, int>> q;
    q.push({ wi,wj });
    visited[wi][wj] = 1;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if (x == si && y == sj) {
            board[si][sj] -= (board[wi][wj]);
            while (true) {
                up[x][y] = false;
                int tmp = parent[x][y][0];
                y = parent[x][y][1];
                x = tmp;
                if (x == wi && y == wj)
                    break;
                if (x < 0 || y < 0 || x >= N || y >= M)
                    cout << x << ' ' << y;
                board[x][y] -= (board[wi][wj] / 2);
            }
            return true;
        }

        for (int k = 0; k < 4; k++) {
            int nx = x + dxy[k][0];
            int ny = y + dxy[k][1];
            if (nx < 0) {
                nx = N - 1;
            }
            if (ny < 0) {
                ny = M - 1;
            }
            if (nx >= N) {
                nx = 0;
            }
            if (ny >= M) {
                ny = 0;
            }

            if (visited[nx][ny] == 0 && board[nx][ny] > 0) {
                visited[nx][ny] = visited[x][y] + 1;
                parent[nx][ny][0] = x;
                parent[nx][ny][1] = y;
                q.push({ nx,ny });
            }
        }
    }
    return false;
}

void boom() {
    for (int k = 0; k < 8; k++) {
        int nx = si + dxy[k][0];
        int ny = sj + dxy[k][1];
        if (nx < 0) {
            nx = N - 1;
        }
        if (ny < 0) {
            ny = M - 1;
        }
        if (nx >= N) {
            nx = 0;
        }
        if (ny >= M) {
            ny = 0;
        }

        if (nx == wi && ny == wj)
            continue;

        board[nx][ny] -= (board[wi][wj] / 2);
        up[nx][ny] = false;
    }
    board[si][sj] -= (board[wi][wj]);
}

void arrange() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] < 0) {
                board[i][j] = 0;
            }
            if (board[i][j] > 0 && up[i][j]) {
                board[i][j]++;
            }
        }
    }
}

int main() {

    cin >> N >> M >> K;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }

    for (int k = 1; k <= K; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                up[i][j] = true;
            }
        }

        findWeeker();
        findStronger();

        if (!laserAttack()) {
            boom();
        }

        up[si][sj] = false;
        up[wi][wj] = false;

        arrange();

        attack[wi][wj] = k;

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] > 0) {
                    cnt++;
                }
            }
        }
        if (cnt == 1) {
            break;
        }
    }

    int answer = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] > answer) {
                answer = board[i][j];
            }
        }
    }

    cout << answer;

    return 0;
}
