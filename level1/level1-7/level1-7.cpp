#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
	int answer = 0;

	sort(d.begin(), d.end());
	int cnt = 0;

	for (int i = 0; i < d.size(); i++) {
		budget -= d[i];
		cnt += 1;

		if (budget < 0) {
			cnt -= 1;
			budget += d[i];
			break;
		}
	}

	answer = cnt;

	return answer;
}

int main()
{
	solution(vector<int> { 1, 3, 2, 5, 4 }, 9);
	solution(vector<int> { 2, 2, 3, 3 }, 10);
}