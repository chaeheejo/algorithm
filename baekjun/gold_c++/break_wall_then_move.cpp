//
//  break_wall_then_move.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int N, M;
int board[1000][1000];
bool visited[1000][1000][2] = {false,};

int dxy[][2] = {
    1,0,
    -1,0,
    0,1,
    0,-1
};

int bfs(){
    queue<tuple<int,int,int,bool>> q;
    q.push({0,0,1,false});
    visited[0][0][0] = true;
    
    while(!q.empty()){
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int depth = get<2>(q.front());
        bool wall = get<3>(q.front());
        q.pop();
        
        if(x==N-1 && y==M-1){
            return depth;
        }
        
        for(int k=0;k<4;k++){
            int nx = x+dxy[k][0];
            int ny = y+dxy[k][1];
            
            if(nx<0 || nx>=N || ny<0 || ny>=M)
                continue;
            
            if(board[nx][ny]==1 && wall==false){
                visited[nx][ny][1] = true;
                q.push({nx,ny,depth+1,true});
            }
            else if(board[nx][ny]==0 && visited[nx][ny][wall]==false){
                visited[nx][ny][wall] = true;
                q.push({nx,ny,depth+1,wall});
            }
        }
    }
    
    return -1;
}

int main(){
    
    cin>>N>>M;
    
    for(int i=0;i<N;i++){
        string temp;
        cin>>temp;
        for(int j=0;j<M;j++){
            if(temp[j]=='1'){
                board[i][j] = 1;
            }
        }
    }
    
    cout<<bfs();
    
    return 0;
}
