//
//  balloon_shooting_game.cpp
//  algorithm
//
//  Created by chaehee on 2023/08/20.
//

#include <iostream>
#include <vector>
using namespace std;

int N, answer;
vector<int> balloon;
int DAT[10];

int getScore(int i){
    int score=0;
    int left = i-1;
    int right = i+1;
    
    while(left>-1 && DAT[left]==1){
        left--;
    }
    while(right<N+1 && DAT[right]==1){
        right++;
    }
    
    if(left==-1 && right==N){
        score=balloon[i];
    }
    else if(left==-1){
        score=balloon[right];
    }
    else if(right==N){
        score=balloon[left];
    }
    else{
        score=balloon[left]*balloon[right];
    }
    
    return score;
}

void dfs(int curDepth, int score){
    if(curDepth==N){
        if(answer<score){
            answer=score;
        }
        return;
    }
    for(int i=0;i<N;i++){
        if(DAT[i]==1)
            continue;
        
        int nxtScore=score+getScore(i);
        
        DAT[i]=1;
        dfs(curDepth+1, nxtScore);
        DAT[i]=0;
    }
}

int main(){
    
    int T;
    cin>>T;
    for(int t=1;t<T+1;t++){
        balloon.clear();
        answer=0;
        
        cin>>N;
        for(int i=0;i<N;i++){
            int temp;
            cin>>temp;
            balloon.push_back(temp);
        }
        
        dfs(0,0);
        
        cout<<"#"<<t<<" "<<answer<<"\n";
    }
    
    return 0;
}
