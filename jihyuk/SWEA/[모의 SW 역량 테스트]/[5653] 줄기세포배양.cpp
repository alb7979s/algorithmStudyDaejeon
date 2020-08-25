#include<cstdio>
#include<algorithm>
#include<list>
#include<queue>
#include<memory.h>

using namespace std;

struct SpreadInfo
{
	int r, c, n;
};

const int MAX = 350;

int T;
int N, M, K;
int time;
int raw[MAX][MAX]; // 퍼지는 시간 최소 2초, 최대 시간 300초, 초기 최대 사이즈 50
int grid[MAX][MAX];
bool visited[MAX][MAX];
int dir[4][2] = { {-1, 0}, {1, 0}, {0, 1}, {0, -1} };
list<pair<int, int>> activeList;
list<pair<int, int>> inactiveList;
queue<pair<int, int>> q;
vector<SpreadInfo> v;

void spread()
{
	int qSize = q.size();
	for (int i = 0; i < qSize; i++)
	{
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int dr = r + dir[i][0];
			int dc = c + dir[i][1];

			if (0 == grid[dr][dc])
			{
				v.push_back({dr, dc, raw[r][c]});
				if (false == visited[dr][dc])
				{
					visited[dr][dc] = true;
					inactiveList.push_back({ dr, dc });
				}
			}
		}
	}

	for (int i = 0; i < v.size(); i++)
	{
		if (grid[v[i].r][v[i].c] < v[i].n)
		{
			grid[v[i].r][v[i].c] = raw[v[i].r][v[i].c] = v[i].n;
		}
	}
	v.clear();
}

void solve()
{
	while (time < K)
	{
		list<pair<int, int>>::iterator it;
		int inactiveCnt = inactiveList.size();
		int activeCnt = activeList.size();
		
		it = activeList.begin();
		// 활성 상태 세포
		for (int i = 0; i < activeCnt; i++)
		{
			int r = it->first;
			int c = it->second;

			if (1 == grid[r][c])
			{
				it = activeList.erase(it);
				grid[r][c] = -1;
			}
			else
			{
				grid[r][c]--;
				++it;
			}
		}

		// 세포 확산
		spread();

		// 비활성 상태 세포
		it = inactiveList.begin();
		for (int i = 0; i < inactiveCnt; i++)
		{
			int r = it->first;
			int c = it->second;

			if (1 == grid[r][c])
			{
				it = inactiveList.erase(it);
				grid[r][c] = raw[r][c];
				activeList.push_back({ r,c });
				q.push({ r,c });
			}
			else
			{
				grid[r][c]--;
				++it;
			}
		}

		time++;
	}
}

int main(int argc, char** argv)
{
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d%d%d", &N, &M, &K);

		activeList.clear();
		inactiveList.clear();
		memset(visited, 0, sizeof(bool) * MAX * MAX);
		memset(raw, 0, sizeof(int) * MAX * MAX);
		memset(grid, 0, sizeof(int) * MAX * MAX);
		queue<pair<int, int>> emptyQ;
		swap(q, emptyQ);
		time = 0;

		int r, c;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				r = i + 150;
				c = j + 150;
				scanf("%d", &raw[r][c]);
				if (0 < raw[r][c])
				{
					inactiveList.push_back({r, c});
				}
			}
		}
		memcpy(grid, raw, MAX * MAX * sizeof(int));

		solve();

		printf("#%d %d\n", testCase, activeList.size() + inactiveList.size());
	}

	return 0;
}