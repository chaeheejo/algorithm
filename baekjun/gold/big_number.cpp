//
//  big_number.cpp
//  mincoding_xcode
//
//  Created by chaehee on 2023/08/09.
//

#include <iostream>
#include <stack>
using namespace std;

int N;
stack<pair<int, int>> st;
int result[1000001];

int main() {
    
    cin >> N;
    
    int temp = 0;
    for (int i = 0; i < N; i++) {
        
        cin >> temp;
        if (st.empty()) {
            st.push({ temp, i });
        }
        else {
            if (st.top().first >= temp) {
                st.push({ temp,i });
            }
            else {
                while (!st.empty() && st.top().first < temp) {
                    int idx = st.top().second;
                    result[idx] = temp;
                    st.pop();
                }
                st.push({temp, i});
            }
        }
    }
    
    while (!st.empty()) {
        int idx = st.top().second;
        result[idx] = -1;
        st.pop();
    }
    
    for (int i = 0; i < N; i++) {
        cout << result[i] << ' ';
    }
    
    return 0;
}
