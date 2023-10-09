//
//  dragon_curve.cpp
//  algorithm
//
//  Created by chaehee on 10/9/23.
//

#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int N;
int board[101][101];

int dxy[][2]={
    0,1,
    -1,0,
    0,-1,
    1,0
};

void makeCurve(int i, int j, int d, int g){
    vector<int> curve;
    curve.push_back(d);
    
    for(int k=0;k<g;k++){
        stack<int> st;
        for(int c=0;c<curve.size();c++){
            st.push(curve[c]);
        }
        while(!st.empty()){
            int cur=st.top();
            st.pop();
            
            cur+=1; //0->1, 1->2, 2->3, 3->4
            if(cur==4){ //3->0
                cur=0;
            }
            curve.push_back(cur);
        }
    }
    
    board[i][j]=1;
    for(int c=0;c<curve.size();c++){
        i+=dxy[curve[c]][0];
        j+=dxy[curve[c]][1];
        board[i][j]=1;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin>>N;
    
    for(int i=0;i<N;i++){
        int x,y,d,g;
        cin>>y>>x>>d>>g;
        makeCurve(x,y,d,g);
    }
    
    int answer=0;
    for(int i=0;i<100;i++){
        for(int j=0;j<100;j++){
            if(board[i][j] && board[i+1][j] && board[i][j+1] && board[i+1][j+1])
                answer++;
        }
    }
    
    cout<<answer;
    
    return 0;
}
