//
//  gear.cpp
//  algorithm
//
//  Created by chaehee on 10/5/23.
//

#include <iostream>
using namespace std;

int K;
int board[4][8];
int cmd[4];

void rotate(int num, bool d) { //num을 d 방향으로 회전
    if (!d) { //right
        int temp = board[num][7];
        for (int i = 7; i > 0; i--) {
            board[num][i] = board[num][i - 1];
        }
        board[num][0] = temp;
    }
    else { //left
        int temp = board[num][0];
        for (int i = 0; i < 7; i++) {
            board[num][i] = board[num][i + 1];
        }
        board[num][7] = temp;
    }
}

void check(int num, bool d) {
    int left = num;
    bool ld = !d;
    while (left - 1 > -1) {
        if ((board[left][6] ^ board[left - 1][2]) == 1) {
            cmd[left - 1] = ld;
        }
        else {
            break;
        }
        left--;
        ld = !ld;
    }

    int right = num;
    bool rd = !d;
    while (right + 1 < 4) {
        if ((board[right][2] ^ board[right + 1][6]) == 1) {
            cmd[right + 1] = rd;
        }
        else {
            break;
        }
        right++;
        rd = !rd;
    }
}

int main() {

    for (int i = 0; i < 4; i++) {
        string temp;
        cin >> temp;

        for (int j = 0; j < 8; j++) {
            if (temp[j] == '1') board[i][j] = 1;
        }
    }

    cin >> K;

    for (int i = 0; i < K; i++) {
        int n, d;
        cin >> n >> d;

        n--;
        if (d == -1) {
            d = 1; //left
        }
        else {
            d = 0;
        }

        for (int i = 0; i < 4; i++) {
            cmd[i] = -1;
        }

        check(n, d);

        for (int i = 0; i < 4; i++) {
            if (cmd[i] != -1) {
                rotate(i, cmd[i]);
            }
        }

        rotate(n, d);
    }

    int answer = 0;
    if (board[0][0]) {
        answer += 1;
    }
    if (board[1][0]) {
        answer += 2;
    }
    if (board[2][0]) {
        answer += 4;
    }
    if (board[3][0]) {
        answer += 8;
    }

    cout << answer;

    return 0;
}
