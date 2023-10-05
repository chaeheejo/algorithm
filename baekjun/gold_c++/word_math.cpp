#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

struct word {
    int idx;
    int priority;

    word(int a, int b) {
        idx = a;
        priority = b;
    }

    bool operator<(const word w) const {
        return this->priority > w.priority;
    }
};

int main() {

    int N;
    cin >> N;

    int dat[27] = { 0, };
    string temp[11];

    for (int i = 0; i < N; i++) {
        cin >> temp[i];

        for (int j = 0; j < temp[i].size(); j++) {
            dat[temp[i][j] - 'A'] += pow(10, temp[i].size() - j);
        }
    }

    vector<word> words;
    for (int i = 0; i < 27; i++) {
        if (dat[i] == 0) {
            continue;
        }

        word cur = word(i, dat[i]);
        words.push_back(cur);
    }

    sort(words.begin(), words.end());

    int answer = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < temp[i].size(); j++) {
            for (int k = 0; k < words.size(); k++) {
                if (temp[i][j]-'A' == words[k].idx) {
                    answer+= pow(10, temp[i].size()-j-1) * (9 - k);
                }
            }
        }
    }

    cout << answer;

    return 0;
}
