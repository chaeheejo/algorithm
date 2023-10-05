//
//  surveillance.cpp
//  algorithm
//
//  Created by chaehee on 10/5/23.
//

#include <iostream>
using namespace std;

int N, M, C, answer;
int board[8][8];
int visited[8][8];
int cctv[8][2];
int path[8];

int dxy[][2] = {
    0,1, //right
    0,-1, //left
    1,0, //up
    -1,0 //down
};

void visitStraight(int k, int x, int y) {
    int nx = x + dxy[k][0];
    int ny = y + dxy[k][1];
    while (1) {
        if (nx < 0 || nx >= N || ny < 0 || ny >= M)
            break;
        if (board[nx][ny] == -1)
            break;
        visited[nx][ny] = 1;
        nx += dxy[k][0];
        ny += dxy[k][1];
    }
}

void spreadCctv() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            visited[i][j] = 0;
        }
    }

    int x, y, mode, k;
    for (int i = 0; i < C; i++) {
        x = cctv[i][0];
        y = cctv[i][1];
        mode = board[x][y];
        k = path[i];

        if (mode == 1) {
            visitStraight(k, x, y);
        }
        else if (mode == 2) {
            if (k == 1) {
                visitStraight(0, x, y);
                visitStraight(1, x, y);
            }
            else {
                visitStraight(2, x, y);
                visitStraight(3, x, y);
            }
        }
        else if (mode == 3) {
            if (k == 1) {
                visitStraight(0, x, y);
                visitStraight(2, x, y);
            }
            else if(k==2) {
                visitStraight(1, x, y);
                visitStraight(3, x, y);
            }
            else if(k==3){
                visitStraight(1, x, y);
                visitStraight(2, x, y);
            }
            else{
                visitStraight(0, x, y);
                visitStraight(3, x, y);
            }
        }
        else if (mode == 4) {
            for (int t = 0; t < 4; t++) {
                if (k == t) continue;
                visitStraight(t, x, y);
            }
        }
        else {
            for (int t = 0; t < 4; t++) {
                visitStraight(t, x, y);
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (visited[i][j] == 0 && board[i][j] == 0) {
                cnt++;
            }
        }
    }
    if (answer > cnt) {
        answer = cnt;
    }
}

void dfs(int curIdx) {
    if (curIdx == C) {
        spreadCctv();
        return;
    }

    int x = cctv[curIdx][0];
    int y = cctv[curIdx][1];
    int mode = board[x][y];
    if(mode==2){
        for (int k = 0; k < 2; k++) {
            path[curIdx] = k;
            dfs(curIdx + 1);
        }
    }
    else{
        for (int k = 0; k < 4; k++) {
            path[curIdx] = k;
            dfs(curIdx + 1);
        }
    }
}

int main() {

    cin >> N >> M;

    answer = 2e9;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int temp;
            cin >> temp;

            if (temp == 6) {
                board[i][j] = -1;
            }
            else if (temp >= 1) {
                cctv[C][0] = i;
                cctv[C][1] = j;
                C++;

                board[i][j] = temp;
            }
            visited[i][j] = temp;
        }
    }

    dfs(0);

    cout << answer;

    return 0;
}
