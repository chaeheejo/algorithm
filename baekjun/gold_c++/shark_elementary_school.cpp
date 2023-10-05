#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
int board[20][20];
vector<int> favorite[400];
vector<int> check[401];

int dxy[][2] = {
	1,0,
	-1,0,
	0,1,
	0,-1
};

struct Area {
	int like;
	int blank;
	int i;
	int j;

	bool operator<(const Area right) const {
		if (like < right.like) return false;
		else if (like > right.like) return true;
		else {
			if (blank < right.blank) return false;
			else if (blank > right.blank) return true;
			else {
				if (i < right.i) return true;
				else if (i > right.i) return false;
				else {
					if (j < right.j) return true;
					else if (j > right.j) return false;
					else return false;
				}
			}
		}
	}
};

int main() {

	cin >> N;

	for (int i = 0; i < N * N; i++) {
		int student;
		cin >> student;
		favorite[i].push_back(student);
		for (int j = 0; j < 4; j++) {
			int temp;
			cin >> temp;
			favorite[i].push_back(temp);
			check[student].push_back(temp);
		}
	}

	for (int n = 0; n < N*N; n++) {
		vector<Area> candidate;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] != 0) {
					continue;
				}

				Area cur = { 0,0,i,j };
				
				for (int k = 0; k < 4; k++) {
					int nx = i + dxy[k][0];
					int ny = j + dxy[k][1];

					if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
						continue;
					}
					
					if (board[nx][ny] == 0) {
						cur.blank++;
					}
					else {
						for (int t = 1; t < 5; t++) {
							if (favorite[n][t] == board[nx][ny]) {
								cur.like++;
							}
						}
					}
				}
				candidate.push_back(cur);
			}
		}

		sort(candidate.begin(), candidate.end());
		board[candidate[0].i][candidate[0].j] = favorite[n][0];
	}

	int answer = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int like = 0;
			for (int k = 0; k < 4; k++) {
				int nx = i + dxy[k][0];
				int ny = j + dxy[k][1];

				if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
					continue;
				}

				for (int t = 0; t < 4; t++) {
					if (check[board[i][j]][t] == board[nx][ny]) {
						like++;
					}
				}
			}
			if (like > 0) {
				int cur = pow(10, like - 1);
				answer += cur;
			}
		}
	}

	cout << answer;

	return 0;
}