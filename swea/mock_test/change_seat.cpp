//
//  change_seat.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N, K, answer;
vector<int> heights;
vector<int> path;
int DAT[20];

void dfs(){
    if(path.size()==N){
        answer++;
        return;
    }
    
    if(path.size()==0){
        for(int i=0;i<N;i++){
            path.push_back(i);
            DAT[i]=1;
            dfs();
            path.pop_back();
            DAT[i]=0;
        }
    }
    else{
        for(int i=0;i<N;i++){
            if(path[path.size()-1]==i || DAT[i]==1){
                continue;
            }
            int past = heights[path[path.size()-1]];
            if(past==heights[i]){
                continue;
            }
            else if(abs(past-heights[i])>K){
                continue;
            }
            path.push_back(i);
            DAT[i]=1;
            dfs();
            path.pop_back();
            DAT[i]=0;
        }
    }
}

int main(){
    
    cin>>N>>K;
    
    for(int i=0;i<N;i++){
        int temp;
        cin>>temp;
        heights.push_back(temp);
    }
    
    dfs();
    
    cout<<answer;
    
    return 0;
}
