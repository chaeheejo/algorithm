//
//  red_green_color_blindness.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int N;
int board[100][100];
int visited[100][100] = {0,};
int dxy[][2] = {
    0,1,
    0,-1,
    1,0,
    -1,0
};

void bfs(int i, int j){
    queue<pair<int,int>> q;
    q.push({i,j});
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int k=0;k<4;k++){
            int nx = x+dxy[k][0];
            int ny = y+dxy[k][1];
            
            if(nx<0 || nx>=N || ny<0 || ny>=N)
                continue;
            
            if(visited[nx][ny]==0){
                if(board[i][j]==board[nx][ny]){
                    visited[nx][ny]=1;
                    q.push({nx,ny});
                }
            }
        }
    }
}

int main(){
    
    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            char temp;
            cin>>temp;
            
            if(temp=='R'){
                board[i][j] = 1;
            }
            else if(temp=='G'){
                board[i][j] = 2;
            }
            else{
                board[i][j] = 3;
            }
        }
    }
    
    int cnt=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(visited[i][j]==0){
                bfs(i, j);
                cnt++;
            }
        }
    }
    cout<<cnt<<' ';
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            visited[i][j]=0;
            if(board[i][j]==2){
                board[i][j]=1;
            }
        }
    }
    
    cnt=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(visited[i][j]==0){
                bfs(i, j);
                cnt++;
            }
        }
    }
    
    cout<<cnt;
    
    return 0;
}
