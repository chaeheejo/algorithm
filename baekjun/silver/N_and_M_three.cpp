//
//  N_and_M_three.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<int> path;

void backtracking(){
    if(path.size()==M){
        for(int i=0;i<path.size();i++){
            cout<<path[i]<<' ';
        }
        cout<<"\n";
        return;
    }
    
    for(int i=1;i<=N;i++){
        path.push_back(i);
        backtracking();
        path.pop_back();
    }
}

int main(){
    
    cin>>N>>M;
    
    backtracking();
    
    return 0;
}
