//
//  connect_processor.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/27.
//

#include <iostream>
#include <vector>
#include <utility>
using namespace std;

int N, maxNum, answer;
int board[12][12];
vector<pair<int,int>> loc;

int dxy[][2] = {
    0,1,
    0,-1,
    1,0,
    -1,0
};

void changeValue(int i, int j, int d, int v){
    int nx=i;
    int ny=j;
    while (true) {
        nx+=dxy[d][0];
        ny+=dxy[d][1];
        if(nx<0 || nx>=N || ny<0 || ny>=N)
            break;
        board[nx][ny]=v;
    }
}

int countBlank(int i, int j, int d){
    int nx=i;
    int ny=j;
    int cnt = 0;
    while (true) {
        nx+=dxy[d][0];
        ny+=dxy[d][1];
        cnt++;
        
        if(board[nx][ny]==1 || board[nx][ny]==2)
            return -1;
        
        if(board[nx][ny]==0 &&(nx==0 || nx==N-1 || ny==0 || ny==N-1))
            return cnt;
    }
}

void dfs(int idx, int curLen, int curNum){
    if(idx==loc.size()){
        if(curNum>maxNum){
            answer=curLen;
            maxNum=curNum;
        }
        else if(curNum==maxNum){
            answer=min(answer, curLen);
        }
        return;
    }
    
    for(int k=0;k<4;k++){
        int cnt=countBlank(loc[idx].first, loc[idx].second, k);
        if(cnt==-1)
            continue;
        
        changeValue(loc[idx].first, loc[idx].second,k,2);
        dfs(idx+1, curLen+cnt, curNum+1);
        changeValue(loc[idx].first, loc[idx].second,k,0);
    }
    dfs(idx+1,curLen,curNum);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin>>T;
    
    for(int t=1;t<=T;t++){
        maxNum=0;
        answer=1e9;
        
        loc.clear();
        
        cin>>N;
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                cin>>board[i][j];
                if(board[i][j]==0 || i==0 || j==N-1 || i==N-1 || j==0)
                    continue;
                loc.push_back({i,j});
            }
        }
        
        dfs(0,0,0);
        cout<<"#"<<t<<" "<<answer<<"\n";
    }
    
    return 0;
}
