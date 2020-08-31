#include<cstdio>
#include<algorithm>
#include<queue>
#include<memory.h>

using namespace std;

const int TOP = 1 << 0;
const int BOTTOM = 1 << 1;
const int LEFT = 1 << 2;
const int RIGHT = 1 << 3;

int T;
int N, M, R, C, L;
int result;
int board[50][50];
int dx[4] = { -1,1,0,0 }; //상하좌우
int dy[4] = { 0,0,-1,1 };
bool visited[50][50];

int movableValue[4] = { TOP, BOTTOM, LEFT, RIGHT };
int moveOut[8] =
{
	0,
	TOP | BOTTOM | LEFT | RIGHT,
	TOP | BOTTOM,
	LEFT | RIGHT,
	TOP | RIGHT,
	BOTTOM | RIGHT,
	BOTTOM | LEFT,
	TOP | LEFT
};

int moveIn[8] =
{
	0,
	TOP | BOTTOM | LEFT | RIGHT,
	TOP | BOTTOM,
	LEFT | RIGHT,
	BOTTOM | LEFT,
	TOP | LEFT,
	TOP | RIGHT,
	BOTTOM | RIGHT
};

void init()
{
	result = 1;
	memset(board, 0, sizeof(board));
	memset(visited, false, sizeof(visited));
}

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < M;
}

void bfs()
{
	queue <pair <int, int> > q;
	q.push(make_pair(R, C));
	visited[R][C] = true;
	int cnt = 1;

	while (1)
	{
		if (cnt == L)
		{
			break;
		}
		cnt++;

		int qSize = q.size();
		for (int i = 0; i < qSize; i++)
		{
			int r = q.front().first;
			int c = q.front().second;
			q.pop();

			for (int idx = 0; idx < 4; idx++)
			{
				if (moveOut[board[r][c]] & movableValue[idx])
				{
					int dr = r + dx[idx];
					int dc = c + dy[idx];
					if (isIn(dr, dc) && board[dr][dc] && !visited[dr][dc] && (moveIn[board[dr][dc]] & movableValue[idx]))
					{
						visited[dr][dc] = true;
						q.push(make_pair(dr, dc));
						result++;
					}
				}
			}
		}
	}
}

int main(int argc, char** argv)
{
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d %d %d %d %d", &N, &M, &R, &C, &L);

		init();

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				scanf("%d", &board[i][j]);
			}
		}

		bfs();

		printf("#%d %d\n", testCase, result);
	}

	return 0;
}