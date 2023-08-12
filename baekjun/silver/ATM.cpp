//
//  ATM.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/12.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int answer;
vector<int> person;

void count_time(){
    answer+=person[0];
    for(int i=0;i<N-1;i++){
        person[i+1] += person[i];
        answer+=person[i+1];
    }
}

int main(){
    
    cin>>N;
    
    for(int i=0;i<N;i++){
        int temp;
        cin>>temp;
        
        person.push_back(temp);
    }
    
    sort(person.begin(), person.end());
    
    count_time();
    
    cout<<answer;
    
    return 0;
}
