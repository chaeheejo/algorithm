//
//  decorate_rooftop_garden.cpp
//  mincoding_xcode
//
//  Created by chaehee on 2023/08/09.
//

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N;
stack<int> st;

int main() {
    cin >> N;
    
    long long answer = 0;
    for (int i = 0; i < N; i++) {
        int temp;
        cin >> temp;
        
        while (!st.empty()) {
            if (st.top() <= temp) {
                st.pop();
            }
            else {
                break;
            }
        }
        answer += st.size();
        st.push(temp);
    }
    
    cout << answer;
    
    return 0;
}
