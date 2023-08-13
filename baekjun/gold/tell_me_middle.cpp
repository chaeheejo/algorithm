//
//  tell_me_middle.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <queue>
using namespace std;

priority_queue<int, vector<int>, greater<int>> big;
priority_queue<int> small;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    cin>>N;

    int middle;
    cin>>middle;
    cout<<middle<<"\n";
    
    for(int n=1;n<N;n++){
        int cur;
        cin>>cur;
        
        if(middle<cur){
            big.emplace(cur);
            
        }
        else{
            small.emplace(cur);
        }
        
        if(big.size()>small.size()+1){
            small.emplace(middle);
            middle = big.top();
            big.pop();
        }
        else if(small.size()>big.size()){
            big.emplace(middle);
            middle = small.top();
            small.pop();
        }
        
        cout<<middle<<"\n";
    }
    
    return 0;
}
