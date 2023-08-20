//
//  division _f_districts.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, answer;
int board[8][8] = { 0, };
int visited[8] = { 0, };
int score[8] = { 0, };
int path[8] = { 0, };

int count_score() {
    int a = -1, b = -1;
    int a_score = 0, b_score = 0;


    for (int i = 0; i < N; i++) {
        if (a == -1 || b == -1) {
            if (a == -1) {
                a = visited[i];
                a_score += score[i];
                continue;
            }
            else if (a!=visited[i]) {
                b = visited[i];
                b_score += score[i];
                continue;
            }
        }
        if (a == visited[i]) {
            a_score += score[i];
        }
        else {
            b_score += score[i];
        }
    }

    if (a_score > b_score) {
        return a_score - b_score;
    }
    return b_score - a_score;
}

bool bfs(int x) {
    visited[x] = x;
    queue<int> q;
    q.push(x);
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int i = 0; i < N; i++) {
            if (i == cur) {
                continue;
            }
            if (board[cur][i] == 1 && visited[i] == -1 && path[i] == path[x]) {
                q.push(i);
                visited[i] = x;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        if (path[i] == path[x]) {
            if (visited[i] == -1) {
                return false;
            }
        }
    }
    return true;
}

void dfs(int cur, int cur_depth, int depth) {
    if (cur_depth == depth) {
        for (int i = 0; i < N; i++) {
            visited[i] = -1;
        }
        for (int i = 0; i < N; i++) {
            if (path[i] == 1) {
                if (bfs(i)==false) {
                    return;
                }
                else {
                    break;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            if (path[i] == -1) {
                if (bfs(i)==false) {
                    return;
                }
                else {
                    break;
                }
            }
        }

        int score = count_score();
        if (score < answer) {
            answer = score;
        }

        return;
    }
    
    for (int i = cur; i < N; i++) {
        path[i] = 1;
        dfs(i + 1, cur_depth+1, depth);
        path[i] = -1;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t = 1; t < T + 1; t++) {
        answer = 1e9;
        cin >> N;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> board[i][j];
            }
        }

        for (int i = 0; i < N; i++) {
            cin >> score[i];
        }

        for (int i = 1; i < N; i++) {
            for (int i = 0; i < N; i++) {
                path[i] = -1;
            }

            dfs(0,0,i);
        }

        cout << "#" << t << " " << answer << "\n";
    }

    return 0;
}
