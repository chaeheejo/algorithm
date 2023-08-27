//
//  popping_popping_mine_hunt.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/27.
//

#include <iostream>
#include <queue>
using namespace std;

int N, answer;
int board[300][300];

int dxy[][2]={
    0,1,
    0,-1,
    1,0,
    -1,0,
    -1,-1,
    -1,1,
    1,-1,
    1,1
};

bool cntBlank(int i, int j){
    for(int k=0;k<8;k++){
        int nx=i+dxy[k][0];
        int ny=j+dxy[k][1];
        if(nx<0 || nx>=N || ny<0 || ny>=N)
            continue;
        if(board[nx][ny]==-1)
            return false;
    }
    return true;
}

void bfs(int i, int j){
    int visited[300][300]={0,};
    visited[i][j]=1;
    
    queue<pair<int,int>> q;
    q.push({i,j});
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        if(board[x][y]==0){
            board[x][y]=1;
            answer++;
        }
        
        for(int k=0;k<8;k++){
            int nx=x+dxy[k][0];
            int ny=y+dxy[k][1];
            if(nx<0 || nx>=N || ny<0 || ny>=N)
                continue;
            if(visited[nx][ny]==0){
                visited[nx][ny]=1;
                
                board[nx][ny]=1;
                
                if(cntBlank(nx, ny))
                    q.push({nx,ny});
            }
        }
    }
}

int main(){
    
    int T;
    cin>>T;
    
    for(int t=1;t<=T;t++){
        answer=0;
        cin>>N;
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                char temp;
                cin>>temp;
                
                if(temp=='.'){
                    board[i][j]=0;
                }
                else{
                    board[i][j]=-1;
                }
            }
        }
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(board[i][j]!=0 || !cntBlank(i, j))
                    continue;
                bfs(i,j);
            }
        }
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(board[i][j]==0)
                    answer++;
            }
        }
        
        cout<<"#"<<t<<" "<<answer<<"\n";
    }
    
    return 0;
}
