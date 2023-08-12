//
//  good_word.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <stack>
#include <string>
using namespace std;

int N;

int main(){
    
    cin>>N;
    
    int answer=0;
    for(int i=0;i<N;i++){
        stack<char> st;
        
        string cur;
        cin>>cur;
        
        for(int j=0;j<cur.size();j++){
            if(!st.empty() && st.top()==cur[j]){
                st.pop();
            }
            else{
                st.push(cur[j]);
            }
        }
        
        if(st.empty()){
            answer++;
        }
    }
    
    cout<<answer;
    
    return 0;
}
