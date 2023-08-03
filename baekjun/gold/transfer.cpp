#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, K, M;
int answer = -1;
vector<int> graph[101001];
int visited[101001];

void bfs() {
	queue<int> q;
	q.push(1);
	visited[1] = 1;

	while (!q.empty()) {
		int x = q.front();
		q.pop();

		if (x == N) {
			answer = visited[x];
			return;
		}

		for (int i = 0; i < graph[x].size(); i++) {
			int cur = graph[x][i];
			if (visited[cur] == 0) {
				if (cur > N) {
					visited[cur] = visited[x];
				}
				else {
					visited[cur] = visited[x] + 1;
				}
				q.push(cur);
			}
		}
	}

	return;
}

int main() {

	cin >> N >> K >> M;

	for (int i = 1; i <= M; i++) {
		for (int j = 0; j < K; j++) {
			int temp;
			cin >> temp;
			graph[i + N].push_back(temp);
			graph[temp].push_back(i + N);
		}
	}

	bfs();

	cout << answer;

	return 0;
}