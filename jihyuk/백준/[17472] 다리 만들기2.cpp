#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

struct edge
{
	int from, to, weight;

	bool operator<(const edge& e2)
	{
		return weight < e2.weight;
	}
};

const int NOT_FOUND = -1;
const int WATER = 0;

int N, M;
int raw[10][10];
int dir[4][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
int groupCnt;
vector<edge> edgeInfo;
vector<pair<int, int>> island[8];
int parent[7];

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < M;
}

void bfs(int r, int c, int n)
{
	queue<pair<int, int>> q;
	q.push({ r,c });

	raw[r][c] = n;

	int water = 0;

	while (!q.empty())
	{
		int row = q.front().first;
		int col = q.front().second;
		q.pop();
		water = 0;

		for (int i = 0; i < 4; i++)
		{
			int dr = row + dir[i][0];
			int dc = col + dir[i][1];

			if (!isIn(dr, dc))
			{
				continue;
			}

			if (NOT_FOUND == raw[dr][dc])
			{
				q.push({ dr, dc });
				raw[dr][dc] = n;
			}
			else if (WATER == raw[dr][dc])
			{
				water++;
			}
		}

		if (water)
		{
			island[n].push_back({ row,col });
		}
	}
}

void linkGraph(int groupNo)
{
	int from = groupNo;
	for (size_t i = 0; i < island[groupNo].size(); i++)
	{
		for (int dirIdx = 0; dirIdx < 4; dirIdx++)
		{
			int dr = island[from][i].first + dir[dirIdx][0];
			int dc = island[from][i].second + dir[dirIdx][1];

			int len = 0;
			int to = 0;

			while (isIn(dr, dc) && 0 == raw[dr][dc])
			{
				dr += dir[dirIdx][0];
				dc += dir[dirIdx][1];
				len++;
			}

			if (isIn(dr, dc))
			{
				to = raw[dr][dc];
			}
			if (2 <= len && to)
			{
				edgeInfo.push_back({ from, to, len });
			}
		}
	}
}

void makeSet()
{
	for (int i = 1; i <= groupCnt; i++)
		parent[i] = i;
}

int find(int x)
{
	if (x == parent[x])
		return x;
	else
		return parent[x] = find(parent[x]);
}

void unite(int x, int y)
{
	x = parent[x];
	y = parent[y];
	parent[x] = y;
}

void solve()
{
	makeSet();
	int cnt = 0;
	int sum = 0;
	int u, v;

	for (int i = 0; i < edgeInfo.size(); i++)
	{
		u = edgeInfo[i].from;
		v = edgeInfo[i].to;
		if (find(u) != find(v))
		{
			unite(u, v);
			cnt++;
			sum += edgeInfo[i].weight;
		}

		if (groupCnt - 1 <= cnt)
		{
			printf("%d", sum);
			return;
		}
	}
	printf("-1", sum);
}

int main()
{
	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			scanf("%d", &raw[i][j]);
			if (raw[i][j])
			{
				raw[i][j] = NOT_FOUND;
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (NOT_FOUND == raw[i][j])
			{
				bfs(i, j, ++groupCnt);
			}
		}
	}

	for (int i = 1; i <= groupCnt; i++)
	{
		linkGraph(i);
	}
	sort(edgeInfo.begin(), edgeInfo.end());

	solve();
}