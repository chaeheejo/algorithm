//
//  princess's_garden.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/12.
//

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;


int START = 301;
int END = 1201;
vector<pair<int, int>> flower;

int main(){
    
    int N;
    cin>>N;
    
    for(int i=0;i<N;i++){
        int startMonth, startDay, endMonth, endDay;
        cin >> startMonth >> startDay >> endMonth >> endDay;
        flower.push_back({startMonth*100+startDay, endMonth*100+endDay});
    }
    
    sort(flower.begin(), flower.end());
    
    int answer = 1;
    int curStart = flower[0].first;
    int curEnd = flower[0].second;
    int cur = START;
    for(int i=1;i<N;i++){
        if(flower[i].first<=cur && cur<flower[i].second){
            if(curEnd<flower[i].second){
                curEnd = flower[i].second;
            }
        }
        else{
            if(flower[i].first<=curEnd && curEnd<flower[i].second){
                answer++;
                cur = curEnd;
                curEnd = flower[i].second;
            }
        }
        
        if(curEnd>=END){
            break;
        }
    }
    
    if(curStart<=START && END<=curEnd){
        cout<<answer;
    }
    else{
        cout<<0;
    }
    
    return 0;
}
