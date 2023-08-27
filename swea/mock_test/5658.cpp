//
//  treasure_box_password.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/27.
//

#include <iostream>
#include <set>
#include <cmath>
#include <deque>
using namespace std;

int N, K;
deque<int> board;
set<int> treasure;

void makeTreasure(){
    for(int n=0;n<N/4;n++){ //회전 수
        deque<int> newBoard;
        for(int i=0;i<4;i++){ //네 면을 확인
            int num = 0;
            for(int j=0;j<N/4;j++){
                int top = board.front();
                newBoard.push_back(top);
                board.pop_front();
                num += pow(16,N/4-j-1)*top;
            }
            treasure.insert(num);
        }
        board = newBoard;
        int back = board.back();
        board.pop_back();
        board.push_front(back);
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin>>T;
    
    for(int t=1;t<=T;t++){
        treasure.clear();
        board.clear();
        
        cin>>N>>K;
        
        string temp;
        cin>>temp;
        
        for(int i=0;i<N;i++){
            if(temp[i]>='A' && temp[i]<='F'){
                board.push_back(temp[i]-'A'+10);
            }
            else{
                board.push_back(temp[i]-'0');
            }
        }
        
        makeTreasure();
        
        auto it = treasure.end();
        it = prev(it,K);
        
        cout<<"#"<<t<<" "<<*it<<"\n";
    }
    
    return 0;
}
