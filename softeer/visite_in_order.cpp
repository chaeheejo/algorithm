//
//  visite_in_order.cpp
//  algorithm
//
//  Created by chaehee on 10/5/23.
//

#include <iostream>
using namespace std;

int N, M, answer;
int board[4][4];
int visited[4][4];
int cmd[4][4];

int dxy[][2] = {
    0,1,
    1,0,
    0,-1,
    -1,0
};

void dfs(int x, int y, int cmdIdx) {
    if (cmdIdx == M + 1) {
        answer++;
        return;
    }

    for (int k = 0; k < 4; k++) {
        int nx = x + dxy[k][0];
        int ny = y + dxy[k][1];
        if (nx < 0 || nx >= N || ny < 0 || ny >= N)
            continue;
        if (board[nx][ny] == 1)
            continue;

        if (visited[nx][ny] == 0) {
            if (cmd[nx][ny] == 0) {
                visited[nx][ny] = 1;
                dfs(nx, ny, cmdIdx);
                visited[nx][ny] = 0;
            }
            else {
                if (cmd[nx][ny] == cmdIdx) {
                    visited[nx][ny] = 1;
                    dfs(nx, ny, cmdIdx + 1);
                    visited[nx][ny] = 0;
                }
            }
        }
    }
}

int main() {

    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    int si, sj;
    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y;
        cmd[x-1][y-1] = i + 1;

        if (i == 0) {
            si = x-1;
            sj = y-1;
        }
    }

    visited[si][sj] = 1;
    dfs(si, sj, 2);

    cout << answer;

    return 0;
}
