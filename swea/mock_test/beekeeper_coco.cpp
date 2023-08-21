//
//  beekeeper_coco.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int N, M, answer;
int board[15][15];
int visited[15][15];

int dxy[][2] = {
    0,1,
    1,0,
    -1,0,
    0,-1,
    1,1,
    1,-1,
    -1,-1,
    -1,1
};

void dfs(int x, int y, int score, int depth) {
    if (depth == 4) {
        answer = max(answer, score);
        return;
    }

    for (int k = 0; k < 8; k++) {
        if (y % 2 == 0 && (k == 4 || k == 5)) {
            continue;
        }
        if (y % 2 == 1 && (k == 6 || k == 7)) {
            continue;
        }

        int nx = x + dxy[k][0];
        int ny = y + dxy[k][1];
        if (nx < 0 || nx >= N || ny < 0 || ny >= M)
            continue;
        if (visited[nx][ny] == 0) {
            visited[nx][ny] = 1;
            dfs(nx, ny, score + board[nx][ny], depth + 1);
            visited[nx][ny] = 0;
        }
    }
}

void check_cross(int i, int j) {
    int one = 0, two = 0, three = 0;

    if (i + 1 < N && j + 2 < M) {
        one = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1];
        answer = max(answer, one);
    }
    if (i - 1 > -1 && j + 2 < M) {
        two = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i - 1][j + 1];
        answer = max(answer, two);
    }
    if ((j % 2 == 0) && (i - 1 > -1 && i + 1 < N && j - 1 > -1 && j + 1 < M)) {
        three = board[i][j] + board[i + 1][j] + board[i - 1][j - 1] + board[i - 1][j + 1];
        answer = max(answer, three);
    }
    if ((j % 2 == 1) && (i - 1 > -1 && i + 1 < N && j - 1 > -1 && j + 1 < M)) {
        three = board[i][j] + board[i - 1][j] + board[i + 1][j - 1] + board[i + 1][j + 1];
        answer = max(answer, three);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t = 1; t < T + 1; t++) {
        cin >> N >> M;

        answer = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> board[i][j];
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = 1;
                dfs(i, j, board[i][j], 1);
                visited[i][j] = 0;
                check_cross(i, j);
            }
        }

        cout << "#" << t << " " << answer << "\n";
    }

    return 0;
}
