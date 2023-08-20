//
//  turn_on_the_light.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

int N, M, K, answer;
unsigned short light;
vector<int> button[18];
int DAT[18];

void dfs(int curLight, int curDepth, int depth){
    if(curDepth==depth){
        if(curLight==((1<<N)-1)){
            answer=1;
        }
        return;
    }
    for(int i=0;i<M;i++){
        if(DAT[i]==1){
            continue;
        }
        unsigned short nxt = curLight;
        for(int j=0;j<K;j++){
            nxt^=(1<<button[i][j]);
        }
        DAT[i]=1;
        dfs(nxt, curDepth+1, depth);
        DAT[i]=0;
    }
}

int main(){
    
    cin>>N>>M>>K;
    
    for(int i=1;i<N+1;i++){
        int temp;
        cin>>temp;
        light+=(temp<<(N-i));
    }
    
    for(int i=0;i<M;i++){
        for(int j=0;j<K;j++){
            int temp;
            cin>>temp;
            button[i].push_back(N-temp);
        }
    }
    
    for(int i=1;i<M+1;i++){
        dfs(light,0,i);
        if(answer){
            answer = i;
            break;
        }
    }
    
    if(answer==0){
        answer=-1;
    }
    cout<<answer;
    
    return 0;
}
