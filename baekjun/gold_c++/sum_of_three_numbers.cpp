#include <iostream>
#include <map>

using namespace std;

int main() {

	int N;
	cin >> N;

	int board[1000];
	
	for (int i = 0; i < N; i++) {
		cin >> board[i];
	}

	map<int, bool> dat;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			dat[board[i] + board[j]] = true;
		}
	}

	int result = 0;

	for (int i = 0; i < N; i++) {
		for (int j = i+1; j < N; j++) {
			if (dat.count(board[j] - board[i])) {
				if (board[j] > result) {
					result = board[j];
				}
			}
		}
	}

	cout << result;

	return 0;
}