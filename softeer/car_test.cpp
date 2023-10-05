//
//  car_test.cpp
//  algorithm
//
//  Created by chaehee on 10/5/23.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, Q;
vector<int> board;
int cmd[200000];

int find_index(int num) {
    int left = 0;
    int right = N - 1;
    int mid = 0;
    while (true) {
        if (left > right) {
            break;
        }
        mid = (left + right) / 2;
        if (board[mid] == num) {
            return mid;
        }
        else if (board[mid] < num) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return 0;
}

int main() {

    cin >> N >> Q;

    for (int i = 0; i < N; i++) {
        int temp;
        cin >> temp;
        board.push_back(temp);
    }

    for (int i = 0; i < Q; i++) {
        int temp;
        cin >> temp;
        cmd[i] = temp;
    }

    sort(board.begin(), board.end());

    for (int i = 0; i < Q; i++) {
        int idx = find_index(cmd[i]);
        if (idx <= 0 || idx >= N - 1)
            cout << 0 << "\n";
        else
            cout << idx * (N - 1 - idx) << "\n";
    }

    return 0;
}
