#include <iostream>
#include <vector>
#include <algorithm>

#define MAX    1000001

using namespace std;

enum STATE
{
    ADAPTOR, NORMAL,
};

int N;
vector<int> graph[MAX];
bool visited[MAX] = { false, };
int dp[MAX][2];

void dfs(int node) {

    visited[node] = true;

    dp[node][ADAPTOR] = 1;
    dp[node][NORMAL] = 0;

    for (int i = 0; i < graph[node].size(); i++) {
        int next = graph[node][i];
        if (visited[next]) continue;

        dfs(next);

        dp[node][ADAPTOR] += min(dp[next][ADAPTOR], dp[next][NORMAL]);
        dp[node][NORMAL] += dp[next][ADAPTOR];
    }
}

int main() {
    cin >> N;

    int n1, n2;
    for (int i = 0; i < N - 1; i++) {
        cin >> n1 >> n2;

        graph[n1].push_back(n2);
        graph[n2].push_back(n1);
    }

    dfs(1);

    cout << min(dp[1][ADAPTOR], dp[1][NORMAL]);
}