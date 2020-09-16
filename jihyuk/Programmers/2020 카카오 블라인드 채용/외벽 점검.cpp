#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<memory.h>

using namespace std;

const int INF = 987654321;
int answer = INF;

int solution(int n, vector<int> weak, vector<int> dist)
{
	sort(dist.begin(), dist.end(), greater<int>());

	int len;
	for (int i = 0; i < weak.size(); i++)
	{
		do
		{
			for (int d = 0, w = 0; d < dist.size(); d++) {
				len = weak[w] + dist[d];
				while (weak[w] <= len)
				{
					w++;
					if (w == weak.size())
					{
						break;
					}
				}
				if (w == weak.size())
				{
					if (d + 1 < answer)
					{
						answer = d + 1;
					}
					break;
				}
			}
		} while (next_permutation(dist.begin(), dist.end()));


		int tmp = weak[0] + n;
		for (int j = 1; j < weak.size(); j++)
		{
			weak[j - 1] = weak[j];
		}
		weak[weak.size() - 1] = tmp;
	}

	if (INF == answer)
	{
		return -1;
	}
	return answer;
}