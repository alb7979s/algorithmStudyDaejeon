#include<cstdio>
#include<memory.h>
#include<algorithm>

using namespace std;

int T, N;
int board[20][20];
bool visited[101];
int maxPathLength;
int dx[] = { 1,-1,-1,1 };
int dy[] = { 1,1,-1,-1 };
int sr, sc;

void init()
{
	memset(visited, 0, sizeof(bool) * 101);
	maxPathLength = -1; // 경로가 존재하지 않는 경우
}

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

void dfs(int r, int c, int dir, int cnt)
{
	if (r == sr - 1 && c == sc + 1 && 4 <= cnt)
	{
		if (maxPathLength < cnt)
		{
			maxPathLength = cnt;
		}
		return;
	}

	for (int i = dir; i < 4; i++)
	{
		int dr = r + dx[i];
		int dc = c + dy[i];

		if (isIn(dr, dc) && false == visited[board[dr][dc]] && i - dir <= 1)
		{
			visited[board[dr][dc]] = true;
			dfs(dr, dc, i, cnt + 1);
			visited[board[dr][dc]] = false;
		}
	}
}

void solve()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			sr = i;
			sc = j;
			visited[board[i][j]] = true;
			dfs(i, j, 0, 1);
			visited[board[i][j]] = false;
		}
	}
}

int main()
{
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d", &N);

		init();

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				scanf("%d", &board[i][j]);
			}
		}

		solve();

		printf("#%d %d\n", testCase, maxPathLength);
	}

	return 0;
}