//
//  apple_eating_game.cpp
//  mincoding_xcode
//
//  Created by chaehee on 2023/08/06.
//

#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;

int N, answer;
int cur_i=0, cur_j=1, cur_d;
int board[10][10];
int dxy[][2]={
    0,1,
    1,0,
    0,-1,
    -1,0
};

void move(int di, int dj){
    int visited[10][10]={0,};
    visited[cur_i][cur_j]=1;
    
    queue<tuple<int, int, int, int>>q;
    q.push({cur_i, cur_j, cur_d, 0});
    
    while(!q.empty()){
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int d = get<2>(q.front());
        int score = get<3>(q.front());
        q.pop();
        
        if(x==di && y==dj){
            cur_i=x;
            cur_j=y;
            cur_d=d;
            answer+=score;
            break;
        }
        
        for(int k=0;k<2;k++){
            int nx = x+dxy[(d+k)%4][0];
            int ny = y+dxy[(d+k)%4][1];
            if(nx<0 || nx>=N || ny<0 || ny>=N)
                continue;
            if(visited[nx][ny]<3){
                visited[nx][ny]++;
                if(k==1){
                    score++;
                }
                q.push({nx,ny,(d+k)%4,score});
            }
        }
    }
}

int main(){
    
    int T=0;
    cin>>T;
    
    for(int t=1;t<=T;t++){
        answer=0;
        cur_i=0;
        cur_j=1;
        cur_d=0;
        cin>>N;
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                cin>>board[i][j];
            }
        }
        
        int M=0;
        int loc[10][2]={0,};
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(board[i][j]==0)
                    continue;
                
                loc[board[i][j]-1][0] = i;
                loc[board[i][j]-1][1] = j;
                
                if(M<board[i][j])
                    M = board[i][j];
            }
        }
        
        for(int i=0;i<M;i++){
            move(loc[i][0], loc[i][1]);
        }
        
        cout<<"#"<<t<<" "<<answer<<endl;
    }
    
    return 0;
}
