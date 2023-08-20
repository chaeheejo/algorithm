//
//  mountain_rescue_robot.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <tuple>
#include <queue>
#include <cmath>
using namespace std;

struct Node{
    int i;
    int j;
    int cost;
    
    bool operator<(const Node right) const{
        if(cost<=right.cost) return false;
        else return true;
    }
};

int N, answer;
int board[30][30];
int dist[30][30];
int dxy[][2] = {
    0,1,
    0,-1,
    1,0,
    -1,0
};

void dijkstra(){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            dist[i][j]=1e9;
        }
    }
    
    priority_queue<Node> pq;
    pq.push({0,0,0});
    dist[0][0]=0;
    while(!pq.empty()){
        Node cur = pq.top();
        pq.pop();
        
        if(cur.i==N-1 && cur.j==N-1){
            answer = min(answer, dist[cur.i][cur.j]);
        }
        
        if(dist[cur.i][cur.j]<cur.cost){
            continue;
        }
        
        for(int k=0;k<4;k++){
            int nx = cur.i+dxy[k][0];
            int ny = cur.j+dxy[k][1];
            
            if(nx<0 || nx>=N || ny<0 || ny>=N)
                continue;
            
            int step=0;
            if(board[cur.i][cur.j]<board[nx][ny]){
                step = (board[nx][ny]-board[cur.i][cur.j])*2;
            }
            else if(board[cur.i][cur.j]==board[nx][ny]){
                step = 1;
            }
            
            if(dist[nx][ny]<dist[cur.i][cur.j]+step){
                continue;
            }
            
            dist[nx][ny] = dist[cur.i][cur.j]+step;
            pq.push({nx,ny,dist[cur.i][cur.j]+step});
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t=1;t<T+1;t++) {
        answer=1e9;
        
        cin >> N;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                cin>>board[i][j];
            }
        }

        dijkstra();
        
        cout<<"#"<<t<<" "<<answer<<"\n";
    }

    return 0;
}
