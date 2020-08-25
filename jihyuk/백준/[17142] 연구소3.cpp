#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<memory.h>

using namespace std;

const int INF = 987654321;

int N, M;
int lab[50][50];
bool visited[50][50];
int dir[4][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
vector<pair<int, int>> virus;
vector<int> pick;
int totalCnt;
int minTime = INF;

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

void bfs()
{
	int restCnt = 0;
	int time = 0;
	queue<pair<int, int>> q;

	// 처음 활성화된 바이러스 큐에 삽입
	for (size_t i = 0; i < pick.size(); i++)
	{
		q.push({ virus[pick[i]].first, virus[pick[i]].second });
		visited[virus[pick[i]].first][virus[pick[i]].second] = true;
	}

	while (q.size() && restCnt < totalCnt)
	{
		int qSize = q.size();
		for (int k = 0; k < qSize; k++)
		{
			int r = q.front().first;
			int c = q.front().second;
			q.pop();

			for (int i = 0; i < 4; i++)
			{
				int dr = r + dir[i][0];
				int dc = c + dir[i][1];

				// 경계를 벗어나거나, 벽이거나, 이미 방문한 경우
				if (!isIn(dr, dc) || 1 == lab[dr][dc] || true == visited[dr][dc])
				{
					continue;
				}
				if (0 == lab[dr][dc])
				{
					restCnt++;
				}
				q.push({ dr, dc });
				visited[dr][dc] = true;
			}
		}
		time++;
	}

	// 모든 빈 공간을 채울 경우, 최소 시간을 비교해서 갱신해준다. 
	if (restCnt == totalCnt && time < minTime)
	{
		minTime = time;
	}
}

void combination(int n, int k)
{
	if (n == M)
	{
		memset(visited, 0, sizeof(visited));
		bfs();
		return;
	}

	for (int i = k; i < virus.size(); i++)
	{
		pick.push_back(i);
		combination(n + 1, i + 1);
		pick.pop_back();
	}
}

int main()
{
	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &lab[i][j]);
			if (0 == lab[i][j])
			{
				totalCnt++;
			}
			else if (2 == lab[i][j])
			{
				virus.push_back({ i,j });
			}
		}
	}

	combination(0, 0);

	if (INF == minTime)
	{
		printf("-1");
	}
	else
	{
		printf("%d", minTime);
	}
}