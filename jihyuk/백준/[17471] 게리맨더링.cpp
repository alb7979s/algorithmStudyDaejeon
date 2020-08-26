#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int N;
bool edge[10][10];
int population[10];
bool visited[10];
int cntComponent;
int s[2];
int minDiff = 987654321;
vector<int> v1, v2;

void bfs(int start, int n)
{
	queue<int> q;
	visited[start] = true;
	q.push(start);

	while (!q.empty())
	{
		int v = q.front();
		s[n] += population[v];

		q.pop();

		for (int i = 0; i < N; i++)
		{
			if (false == visited[i] && true == edge[v][i])
			{
				visited[i] = true;
				q.push(i);
			}
		}
	}
}

bool checkConnected(vector<int>& picked)
{
	size_t cnt = 0;

	queue<int> q;
	bool visitedArea[10] = { false };
	q.push(picked[0]);
	visitedArea[picked[0]] = true;
	cnt++;

	while (!q.empty())
	{
		int v = q.front();

		q.pop();

		for (int i = 0; i < picked.size(); i++)
		{
			int idx = picked[i];
			if (false == visitedArea[idx] && true == edge[v][idx])
			{
				cnt++;
				visitedArea[idx] = true;
				q.push(idx);
			}
		}
	}

	return cnt == picked.size();
}

void combination(int n)
{
	if (0 == n)
	{
		v1.clear();
		v2.clear();
		for (int i = 0; i < N; i++)
		{
			if (visited[i])
			{
				v1.push_back(i);
			}
			else
			{
				v2.push_back(i);
			}
		}

		if (checkConnected(v1) && checkConnected(v2))
		{
			int sum = 0;
			for (size_t i = 0; i < v1.size(); i++)
			{
				sum += population[v1[i]];
			}
			if (abs(s[0] - 2 * sum) < minDiff)
			{
				minDiff = abs(s[0] - 2 * sum);
			}
		}

		return;
	}

	for (int i = 0; i < N; i++)
	{
		if (visited[i])
		{
			continue;
		}
		visited[i] = true;
		combination(n - 1);
		visited[i] = false;
	}
}

void findMinDiff()
{
	fill(visited, visited + 10, false);
	v1.reserve(N);
	v2.reserve(N);
	int selectCount = (N + 1) / 2;
	for (int i = 1; i <= selectCount; i++)
	{
		combination(i);
	}
	printf("%d", minDiff);
}

int main()
{
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &population[i]);
	}

	for (int i = 0, cnt, v; i < N; i++)
	{
		scanf("%d", &cnt);
		for (int j = 0; j < cnt; j++)
		{
			scanf("%d", &v);
			v--;
			edge[i][v] = edge[v][i] = true;
		}
	}

	for (int i = 0; i < N; i++)
	{
		if (false == visited[i])
		{
			if (1 < cntComponent)
			{
				printf("-1");
				return 0;
			}
			bfs(i, cntComponent);
			cntComponent++;
		}
	}

	if (1 == cntComponent)
	{
		findMinDiff();
	}
	else
	{
		printf("%d", abs(s[0] - s[1]));
	}
}