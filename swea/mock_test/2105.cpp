//
//  2105.cpp
//  mincoding_xcode
//
//  Created by chaehee on 2023/07/30.
//

#include <iostream>
using namespace std;

int N, answer;
int board[21][21];
int dxy[][2]={
    -1,1,
    1,1,
    1,-1,
    -1,-1
};

int make_square(int x, int y, int rlen, int clen){
    int flag=1;
    int dessert[101] = {0,};
    int nx = x, ny = y;
    int nx = x, ny = y;
    
    for(int k=0;k<4;k++){
        int times=0;
        if(k%2==0)
            times = rlen;
        else
            times = clen;
        
        for(int n=0;n<times;n++){
            nx+=dxy[k][0];
            ny+=dxy[k][1];
            if(nx<0 || nx>=N || ny<0 || ny>=N){
                flag=0;
                break;
            }
            if(dessert[board[nx][ny]]!=0){
                flag=0;
                break;
            }
            dessert[board[nx][ny]]=1;
        }
        if(!flag)
            break;
    }
    
    if(flag){
        int cnt =0;
        for(int i=0;i<101;i++){
            if(dessert[i]==0)
                continue;
            cnt++;
        }
        return cnt;
    }
    
    return -1;
}

int count_dessert(int x, int y){
    int rtn=-1;
    for(int w=1;w<=N;w++){
        for(int h=1;h<=N;h++){
            int cur = make_square(x,y,w,h);
            if(cur>rtn){
                rtn = cur;
            }
        }
    }
    return rtn;
}

int main(){
    int T;
    cin>>T;
    
    for(int t=0;t<T;t++){
        cin>>N;
        answer=-1;
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                cin>>board[i][j];
            }
        }
        
        for(int i=1;i<N-1;i++){
            for(int j=0;j<N-2;j++){
                int cur = count_dessert(i,j);
                if(cur>answer){
                    answer = cur;
                }
            }
        }
        
        printf("#%d %d\n", t+1, answer);
    }
}
