//
//  famous_seven_princesses.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define N 5

int answer;
char board[5][5];

int dxy[][2] = {
    1,0,
    0,1,
    -1,0,
    0,-1
};

vector<int> path;

bool isConnected(){
    int lee = 0;
    int visited[N][N] = {0,};
    
    for(int i=0;i<7;i++){
        int x = (path[i]-1)/N;
        int y = (path[i]-1)%N;
        visited[x][y] = 1;
        
        if(board[x][y]=='S'){
            lee++;
        }
    }
    
    if(lee<4)
        return false;
    
    
    queue<pair<int, int>> q;
    q.push({(path[0]-1)/N, (path[0]-1)%N});
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int k=0;k<4;k++){
            int nx = x+dxy[k][0];
            int ny = y+dxy[k][1];
            
            if(nx<0 || nx>=N || ny<0 || ny>=N)
                continue;
            
            if(visited[nx][ny]==1){
                visited[nx][ny]=0;
                q.push({nx,ny});
            }
        }
    }
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(visited[i][j]){
                return false;
            }
        }
    }
    return true;
}

void backtracking(int cur){
    if(path.size()==7){
        if(isConnected()){
            answer++;
        }
        return;
    }
    
    for(int i=cur+1;i<26;i++){
        path.push_back(i);
        backtracking(i);
        path.pop_back();
    }
}

int main(){
    
    for(int i=0;i<N;i++){
        string temp;
        cin>>temp;
        for(int j=0;j<N;j++){
            board[i][j] = temp[j];
        }
    }
    
    for(int i=1;i<26-6;i++){
        path.push_back(i);
        backtracking(i);
        path.pop_back();
    }
    
    cout<<answer;
    
    return 0;
}
