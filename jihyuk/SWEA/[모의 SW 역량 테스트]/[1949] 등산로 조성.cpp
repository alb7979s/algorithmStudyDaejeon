#include<cstdio>
#include<algorithm>
#include<queue>
#include<memory.h>

using namespace std;

int T;
int N, K;
int maxPathLength;
int terrain[8][8];
int visited[8][8];
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { 1, -1, 0, 0 };
int highest;

void init()
{
	memset(visited, false, sizeof(visited));
	maxPathLength = 0;
	highest = 0;
}

void input()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &terrain[i][j]);
			if (highest < terrain[i][j])
			{
				highest = terrain[i][j];
			}
		}
	}
}

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

void dfs(int r, int c, int len, int cutCnt)
{
	maxPathLength = max(maxPathLength, len);
	visited[r][c] = true;

    for (int idx = 0; idx < 4; idx++)
	{
        int dr = r + dx[idx];
        int dc = c + dy[idx];

		if (visited[dr][dc] || !isIn(dr, dc))
		{
			continue;
		}

        if (terrain[dr][dc] < terrain[r][c]) // 현재 지형보다 낮은 경우
		{
			dfs(dr, dc, len + 1, cutCnt);
        }
        else // 현재 지형보다 낮지 않은 경우(같거나 높은 경우)
		{
			if (cutCnt == 0 && terrain[dr][dc] - K < terrain[r][c])
			{
				int originHeight = terrain[dr][dc];

				terrain[dr][dc] = terrain[r][c] - 1; // 현재 높이보다 한칸 낮은 높이로 설정한 후 진행
				dfs(dr, dc, len + 1, 1);
				terrain[dr][dc] = originHeight;
			}
        }
    }
	visited[r][c] = false;
}

void solve()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (terrain[i][j] == highest && !visited[i][j])
			{
				visited[i][j] = true;
				dfs(i, j, 1, 0);
				visited[i][j] = false;
			}
		}
	}
}

int main(int argc, char** argv)
{
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d %d", &N, &K);

		init();
		input();
		solve();

		printf("#%d %d\n", testCase, maxPathLength);
	}

	return 0;
}