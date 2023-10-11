//
//  maze_runner.cpp
//  algorithm
//
//  Created by chaehee on 10/9/23.
//

#include <iostream>
#include <cmath>
using namespace std;

int N, M, K, di, dj, step;
int board[10][10];
int person[10][2];
int newBoard[10][10];

int dxy[][2] = {
    1,0,
    -1,0,
    0,-1,
    0,1
};

void movePerson() {
    for (int m = 0; m < M; m++) {
        if (person[m][0] == -1) //이미 탈출
            continue;

        int curDist = abs(di - person[m][0]) + abs(dj - person[m][1]);

        for (int k = 0; k < 4; k++) {
            int nx = person[m][0] + dxy[k][0];
            int ny = person[m][1] + dxy[k][1];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;

            if (board[nx][ny] > 0)
                continue;

            int nextDist = abs(di - nx) + abs(dj - ny);
            if (curDist > nextDist) { //현재 거리보다 작으면
                person[m][0] = nx;
                person[m][1] = ny;
                step++;

                break;
            }
        }
    }
}

void rotate(int x, int y, int n) {
    int visited[10] = { 0, };
    bool visit = true;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            newBoard[x + j][y + n - 1 - i] = board[x + i][y + j];

            for (int m = 0; m < M; m++) {
                if (person[m][0] == -1 || visited[m] == 1)
                    continue;
                if (person[m][0] == x + i && person[m][1] == y + j) { //현재 위치가 person의 위치이면,
                    person[m][0] = x + j;
                    person[m][1] = y + n - 1 - i;
                    visited[m] = 1;
                }
            }

            if (visit) { //탈출 loc
                if (di == x + i && dj == y + j) {
                    di = x + j;
                    dj = y + n - 1 - i;
                    visit = false;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            board[i + x][j + y] = newBoard[i + x][j + y];
            if (board[i + x][j + y] > 0) {
                board[i + x][j + y]--;
            }
        }
    }
}

void findSquare() {
    for (int len = 2; len <= N; len++) { //사각형 크기
        for (int i = 0; i <= N - len; i++) { //시작점 i - i~i+len-1
            for (int j = 0; j <= N - len; j++) { //시작점 j
                //range : i~i+n & j~j+n
                if (di < i || di >= i + len || dj < j || dj >= j + len) //출구를 포함하는지
                    continue;
                for (int m = 0; m < M; m++) {
                    if (person[m][0] == -1)
                        continue;
                    if (person[m][0] >= i && person[m][0] < i + len && person[m][1] >= j && person[m][1] < j + len) {
                        rotate(i, j, len);
                        return;
                    }
                }
            }
        }
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < M; i++) {
        cin >> person[i][0] >> person[i][1];
        person[i][0]--;
        person[i][1]--;
    }

    cin >> di >> dj;
    di--;
    dj--;

    for (int k = 0; k < K; k++) {
        movePerson();

        for (int m = 0; m < M; m++) {
            if (person[m][0] == di && person[m][1] == dj) { //탈출
                person[m][0] = -1;
                person[m][1] = -1;
            }
        }

        findSquare();

        bool flag = true;
        for (int i = 0; i < M; i++) {
            if (person[i][0] != -1) {
                flag = false;
                break;
            }
        }
        if (flag) {
            break;
        }
    }

    cout << step << "\n" << di + 1 << " " << dj + 1;

    return 0;
}
