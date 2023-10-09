//
//  laboratory.cpp
//  algorithm
//
//  Created by chaehee on 10/9/23.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, answer;
int board[8][8];
int DAT[64];
vector<pair<int,int>> virus;

int dxy[][2]={
    0,1,
    1,0,
    -1,0,
    0,-1
};

void simulation(){
    int visited[8][8]={0,};
    
    queue<pair<int,int>> q;
    int x,y;
    for(int i=0;i<virus.size();i++){
        x=virus[i].first;
        y=virus[i].second;
        q.push({x,y});
    }
    
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int k=0;k<4;k++){
            int nx = x+dxy[k][0];
            int ny = y+dxy[k][1];
            if(nx<0 || nx>=N || ny<0 || ny>=M)
                continue;
            if(visited[nx][ny]==0 && board[nx][ny]==0){
                visited[nx][ny]=1;
                q.push({nx,ny});
            }
        }
    }
    
    int cur=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(visited[i][j]==0 && board[i][j]==0){
                cur++;
            }
        }
    }
    
    if(answer<cur){
        answer=cur;
    }
}

void dfs(int curDepth, int cur){
    if(curDepth==3){
        simulation();
        return;
    }
    for(int n=cur;n<N*M;n++){
        if(DAT[n]==1)
            continue;
        
        int x=n/M;
        int y=n%M;
        if(board[x][y]!=0)
            continue;
        
        DAT[n]=1;
        board[x][y]=100;
        dfs(curDepth+1,n+1);
        board[x][y]=0;
        DAT[n]=0;
    }
}

int main(){
    
    cin>>N>>M;
    
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin>>board[i][j];
            
            if(board[i][j]==2){
                virus.push_back({i,j});
                
            }
        }
    }
    
    dfs(0,0);
    
    cout<<answer;
    
    return 0;
}
