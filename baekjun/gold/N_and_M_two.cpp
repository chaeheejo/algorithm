//
//  N_and_M_two.cpp
//  mincoding_xcode
//
//  Created by chaehee on 2023/08/09.
//

#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<int> path;

void backtracking(int cur) {
    if (path.size() == M) {
        for (int i = 0; i < path.size(); i++) {
            cout << path[i] << ' ';
        }
        cout << endl;
    }
    
    for (int i = cur + 1; i <= N; i++) {
        path.push_back(i);
        backtracking(i);
        path.pop_back();
    }
}

int main() {
    
    cin >> N >> M;
    
    backtracking(0);
    
    return 0;
}
