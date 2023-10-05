//
//  paste_color_paper.cpp
//  c++_workspace
//
//  Created by chaehee on 2023/08/12.
//

#include <iostream>
using namespace std;

int N = 10;
int answer=1e9;
int board[10][10];
int paper[5] = {5,5,5,5,5};

bool canPaste(int x, int y, int k){
    for(int i=x;i<=x+k;i++){
        for(int j=y;j<=y+k;j++){
            if(board[i][j]==0)
                return false;
        }
    }
    return true;
}

bool isAllZero(){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(board[i][j])
                return false;
        }
    }
    return true;
}

void fillBoard(int x, int y, int k, int value){
    for(int i=x;i<=x+k;i++){
        for(int j=y;j<=y+k;j++){
            board[i][j]=value;
        }
    }
}

void dfs(int cur){
    if(isAllZero()){
        if(answer>cur){
            answer = cur;
        }
        return;
    }
    if(answer<cur){
        return;
    }
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(board[i][j]){
                for(int k=4;k>-1;k--){
                    if(paper[k]<=0)
                        continue;
                    if(i+k>=10 || j+k>=10)
                        continue;
                    if(!canPaste(i, j, k))
                        continue;
                    
                    paper[k]--;
                    fillBoard(i, j, k, 0);
                    
                    dfs(cur+1);
                    
                    paper[k]++;
                    fillBoard(i, j, k, 1);
                }
                return;
            }
        }
    }
}

int main(){
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>board[i][j];
        }
    }
    
    dfs(0);
    
    if(answer==1e9)
        answer=-1;
    
    cout<<answer;
    
    return 0;
}
