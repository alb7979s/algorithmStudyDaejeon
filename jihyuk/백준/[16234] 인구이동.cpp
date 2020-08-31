#include<cstdio>
#include<algorithm>
#include<queue>
#include<memory.h>

using namespace std;

int N, L, R;
int nation[50][50];
bool visited[50][50];
int days;
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
vector<pair<int, int>> group;
int sum;

void input()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &nation[i][j]);
		}
	}
}

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

void bfs(int r, int c)
{
	queue<pair<int, int>> q;
	q.push({ r,c });
	visited[r][c] = true;
	sum += nation[r][c];
	group.push_back({ r,c });

	int diff;

	while (!q.empty())
	{
		r = q.front().first;
		c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int dr = r + dx[i];
			int dc = c + dy[i];

			int diff = abs(nation[r][c] - nation[dr][dc]);

			if (!isIn(dr, dc) || visited[dr][dc] || diff < L || R < diff)
			{
				continue;
			}

			q.push({ dr, dc });
			visited[dr][dc] = true;
			sum += nation[dr][dc];
			group.push_back({ dr,dc });
		}
	}

}

void solve()
{
	int avg;
	bool check = true;
	days = -1;

	while (check)
	{
		check = false;
		memset(visited, false, sizeof(visited));
		days++;

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (false == visited[i][j])
				{
					group.clear();
					sum = 0;

					bfs(i, j);

					if (1 < group.size())
					{
						avg = sum / group.size();
						for (size_t i = 0; i < group.size(); i++)
						{
							nation[group[i].first][group[i].second] = avg;
						}

						check = true;
					}
				}
			}
		}
	}
}

int main()
{
	scanf("%d %d %d", &N, &L, &R);

	input();
	solve();

	printf("%d", days);

	return 0;
}