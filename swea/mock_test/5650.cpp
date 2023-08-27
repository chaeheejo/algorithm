//
//  pinball_game.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/27.
//

#include <iostream>
#include <vector>
#include <utility>
using namespace std;

int N, answer;
int board[100][100];
vector<pair<int,int>> worm[5];

int dxy[][2]={
    -1,0,
    0,1,
    1,0,
    0,-1
};

int changeDirection(int block, int d){
    if(block==1){
        if(d==0){
            d=2;
        }
        else if(d==1){
            d=3;
        }
        else if(d==2){
            d=1;
        }
        else{
            d=0;
        }
    }
    else if(block==2){
        if(d==0){
            d=1;
        }
        else if(d==1){
            d=3;
        }
        else if(d==2){
            d=0;
        }
        else{
            d=2;
        }
    }
    else if(block==3){
        if(d==0){
            d=3;
        }
        else if(d==1){
            d=2;
        }
        else if(d==2){
            d=0;
        }
        else{
            d=1;
        }
    }
    else if(block==4){
        if(d==0){
            d=2;
        }
        else if(d==1){
            d=0;
        }
        else if(d==2){
            d=3;
        }
        else{
            d=1;
        }
    }
    else{
        d=(d+2)%4;
    }
    return d;
}

void getScore(int si, int sj){
    for(int k=0;k<4;k++){
        int i=si,j=sj,d=k;
        int score=0;
        while(true){
            if(board[i][j]>=6){
                int idx = board[i][j]-6;
                if(worm[idx][0].first==i && worm[idx][0].second==j){
                    i=worm[idx][1].first;
                    j=worm[idx][1].second;
                }
                else{
                    i=worm[idx][0].first;
                    j=worm[idx][0].second;
                }
            }
            else if(board[i][j]>=1){
                d=changeDirection(board[i][j], d);
                score++;
            }
            
            i+=dxy[d][0];
            j+=dxy[d][1];
            
            if(i<0 || i>=N || j<0 || j>=N){
                if(answer<score*2+1){
                    answer=score*2+1;
                }
                break;
            }
            
            if(board[i][j]==-1 ||(i==si && j==sj)){
                if(answer<score){
                    answer=score;
                }
                break;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin>>T;
    
    for(int t=1;t<=T;t++){
        answer=0;
        cin>>N;
        
        for(int i=0;i<5;i++){
            worm[i].clear();
        }
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                cin>>board[i][j];
                
                if(board[i][j]>=6){
                    worm[board[i][j]-6].push_back({i,j});
                }
            }
        }
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(board[i][j]==0){
                    getScore(i,j);
                }
            }
        }
        
        cout<<"#"<<t<<" "<<answer<<"\n";
    }
    
    return 0;
}
