#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;

int N, M;
int answer = 1e9;
int board[51][51];
vector<pair<int, int>> loc;
vector<int> path;

int dxy[][2] = {
	1,0,
	-1,0,
	0,1,
	0,-1
};

void bfs() {
	int visited[51][51] = { 0, };
	for (int m = 0; m < M; m++) {
		int i = loc[path[m]].first;
		int j = loc[path[m]].second;

		queue<tuple<int, int, int>> q;
		q.push({ i,j,1 });
		while (!q.empty()) {
			int x = get<0>(q.front());
			int y = get<1>(q.front());
			int value = get<2>(q.front());
			q.pop();

			for (int k = 0; k < 4; k++) {
				int nx = x + dxy[k][0];
				int ny = y + dxy[k][1];

				if (nx < 0 || nx >= N || ny < 0 || ny >= N)
					continue;

				if (visited[nx][ny] > value || visited[nx][ny]==0) {
					visited[nx][ny] = value;
					if (board[nx][ny] != 1) {
						q.push({ nx,ny,value + 1 });
					}
				}
			}
		}
	}

	int rtn = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (board[i][j] == 1 || board[i][j] == 2) {
				continue;
			}

			if (visited[i][j] == 0) {
				rtn = -1;
				break;
			}

			if (visited[i][j] > rtn) {
				rtn = visited[i][j];
			}
		}
		if (rtn == -1) {
			break;
		}
	}

	if (rtn != -1) {
		if (answer > rtn) {
			answer = rtn;
		}
	}
}

void dfs(int cur) {
	if (path.size() == M) {
		bfs();
		return;
	}
	for (int i = cur; i < loc.size(); i++) {
		path.push_back(i);
		dfs(i+1);
		path.pop_back();
	}
}

int main() {

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int temp;
			cin >> temp;
			board[i][j] = temp;
			if (temp == 2) {
				loc.push_back({ i,j });
			}
		}
	}

	dfs(0);

	if (answer == 1e9) {
		answer = -1;
	}
	cout << answer;

	return 0;
}