//
//  find_landmine.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int N, M, startI, startJ;
char board[50][50];
int visited[50][50];

int dxy[][2] = {
    0,1,
    0,-1,
    1,0,
    -1,0,
    -1,1,
    -1,-1,
    1,-1,
    1,1
};

int checkNeighbor(int x, int y){
    int boom=0;
    for(int k=0;k<8;k++){
        int nx = x+dxy[k][0];
        int ny = y+dxy[k][1];
        if(nx<0 || nx>=N || ny<0 || ny>=M)
            continue;
        if(board[nx][ny]=='M')
            boom++;
    }
    return boom;
}

void bfs(){
    queue<pair<int,int>> q;
    q.push({startI, startJ});
    visited[startI][startJ]=1;
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        if(board[x][y]=='M'){
            board[x][y]='X';
            return;
        }
        else if(board[x][y]=='E'){
            int cnt = checkNeighbor(x,y);
            if(cnt!=0){
                board[x][y] = cnt + '0';
            }
            else{
                board[x][y] = 'B';
                for(int k=0;k<8;k++){
                    int nx = x+dxy[k][0];
                    int ny = y+dxy[k][1];
                    if(nx<0 || nx>=N || ny<0 || ny>=M)
                        continue;
                    if(visited[nx][ny]==0){
                        visited[nx][ny]=1;
                        q.push({nx,ny});
                    }
                }
            }
        }
    }
}

int main(){
    
    cin>>N>>M;
    
    for(int i=0;i<N;i++){
        string temp;
        cin>>temp;
        
        for(int j=0;j<M;j++){
            board[i][j] = temp[j];
        }
    }
    
    cin>>startI>>startJ;
    
    bfs();
    
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cout<<board[i][j];
        }
        cout<<'\n';
    }
    
    
    return 0;
}
