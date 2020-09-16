#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<string, int> m;
vector<int> gemsOrder;
vector<int> pickCnt;

vector<int> solution(vector<string> gems)
{
	vector<int> answer;

	int N = gems.size();

	gemsOrder.reserve(N);

	for (size_t i = 0, idx = 0; i < gems.size(); i++)
	{
		auto it = m.find(gems[i]);
		if (m.end() == it)
		{
			it = m.insert(unordered_map<string, int>::value_type(gems[i], idx++)).first;
		}
		gemsOrder.push_back(it->second);
	}

	int M = m.size();
	pickCnt.resize(M, 0);

	int itemCnt = 0;
	int start = 0, end = 0;
	int minCnt = 987654321;
	answer.resize(2, 0);

	while (end < N)
	{
		if (itemCnt < M)
		{
			if (0 == pickCnt[gemsOrder[end]])
			{
				itemCnt++;
			}
			pickCnt[gemsOrder[end]]++;
			end++;
		}
		while (M == itemCnt)
		{
			if (end - (start + 1) < minCnt)
			{
				minCnt = end - (start + 1);
				answer[0] = start + 1;
				answer[1] = end;
			}
			pickCnt[gemsOrder[start]]--;
			if (0 == pickCnt[gemsOrder[start]])
			{
				itemCnt--;
			}
			start++;
		}
	}

	return answer;
}
/*
int main()
{
	int N;
	cin >> N;
	vector<string> gems;
	gems.resize(N);

	for (int i = 0; i < N; i++)
	{
		cin >> gems[i];
	}
	vector<int> v = solution(gems);
	cout << v[0] << " , " << v[1];

	return 0;
}
*/