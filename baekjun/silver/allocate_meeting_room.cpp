//
//  allocate_meeting_room.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/13.
//

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

vector<pair<int, int>> meeting;

int main(){
    
    int N;
    cin>>N;
    
    for(int i=0;i<N;i++){
        int start, end;
        cin>>start>>end;
        meeting.push_back({start,end});
    }
    
    sort(meeting.begin(), meeting.end());
    
    int answer=1;
    int curEnd = meeting[0].second;
    for(int i=1;i<N;i++){
        if(meeting[i].second<curEnd){
            curEnd = meeting[i].second;
        }
        else if(curEnd<=meeting[i].first){
            answer++;
            curEnd = meeting[i].second;
        }
    }
    
    cout<<answer;
    
    return 0;
}
