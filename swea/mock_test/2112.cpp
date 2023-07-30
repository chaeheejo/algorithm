//
//  2112.cpp
//  mincoding_xcode
//
//  Created by chaehee on 2023/07/30.
//

#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int R, C, K;
bool board[13][20];
bool original_board[13][20];
vector<pair<int, bool>> path;

bool check_cell() {
    for (int j = 0; j < C; j++) {
        int cur = board[0][j];
        int cnt = 1;
        for (int i = 1; i < R; i++) {
            if (cnt == K)
                break;
            if (cur == board[i][j])
                cnt++;
            else {
                cur = board[i][j];
                cnt = 1;
            }
        }
        if (cnt < K)
            return false;
    }
    return true;
}

bool dfs(int cur, int depth) {
    int len = path.size();
    if (len == depth) {
        for(int i=0;i<len;i++){
            memset(board[path[i].first], path[i].second, sizeof(board[path[i].first]));
        }
        if(!check_cell()){
            memcpy(board, original_board, sizeof(board));
            return false;
        }
        return true;
    }
    for (int i = cur; i < R; i++) {
        path.push_back({ i,0 });
        if (dfs(i + 1, depth))
            return true;
        path.pop_back();
        
        path.push_back({ i,1 });
        if (dfs(i + 1, depth))
            return true;
        path.pop_back();
    }
    return false;
}

int main() {
    int T=0;
    cin>>T;
    
    for(int t=0;t<T;t++){
        cin>>R>>C>>K;
        
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                cin>>board[i][j];
                original_board[i][j] = board[i][j];
            }
        }
        
        int answer=K;
        for(int i=0;i<K;i++){
            path.clear();
            if(dfs(0, i)){
                answer = i;
                break;
            }
        }
        
        printf("#%d %d\n", t+1, answer);
    }
    return 0;
}
