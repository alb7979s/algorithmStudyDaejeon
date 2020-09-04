#include<cstdio>
#include<algorithm>
#include<queue>
#include<memory.h>

using namespace std;

int N, M, K;
int microbe[1001];
int tmpMicrobe[1001];
int microbeDir[1001];
int remainCnt;
int board[100][100]; // 몇번 째 미생물이 있는지 저장
int timeBoard[100][100];
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
queue<pair<int, int>> q;

void init()
{
	remainCnt = 0;
	memset(board, 0, sizeof(board)); 
	memset(timeBoard, 0, sizeof(timeBoard));
	memset(microbe, 0, sizeof(microbe));
	memset(tmpMicrobe, 0, sizeof(tmpMicrobe));
	memset(microbeDir, 0, sizeof(microbeDir));
	q = queue<pair<int, int>>();
}

void input()
{
	scanf("%d%d%d", &N, &M, &K);

	int r, c, n, dir;
	for (int i = 1; i <= K; i++)
	{
		scanf("%d %d %d %d", &r, &c, &n, &dir);
		tmpMicrobe[i] = microbe[i] = n;
		microbeDir[i] = dir - 1;
		board[r][c] = i;
		q.push({ r,c });
		remainCnt += n;
	}
}

bool isCollisionWall(int r, int c)
{
	return 0 == r || N - 1 == r || 0 == c || N - 1 == c;
}

void bfs()
{
	struct MoveInfo
	{
		int r, c, idx;
	};
	queue<MoveInfo> moveQ;

	int time = 0;
	while (time < M && 0 < remainCnt)
	{
		int qsize = q.size();
		time++;

		for (int i = 0; i < qsize; i++)
		{
			int r = q.front().first;
			int c = q.front().second;
			q.pop();

			int idx = board[r][c];
			microbe[idx] = tmpMicrobe[idx];
			int dir = microbeDir[idx];

			int nr = r + dr[dir];
			int nc = c + dc[dir];

			if (isCollisionWall(nr, nc))
			{
				remainCnt -= (microbe[idx] + 1) >> 1;
				tmpMicrobe[idx] = microbe[idx] = microbe[idx] >> 1;
				microbeDir[idx] = (microbeDir[idx] & 1) ? microbeDir[idx] - 1 : microbeDir[idx] + 1;
			}

			board[r][c] = 0;
			if (0 < microbe[idx])
			{
				moveQ.push({ nr, nc, idx });
			}
		}

		while (!moveQ.empty())
		{
			int r = moveQ.front().r;
			int c = moveQ.front().c;
			int idx = moveQ.front().idx;

			moveQ.pop();
			
			if (timeBoard[r][c] < time)
			{
				timeBoard[r][c] = time;
				board[r][c] = idx;
				tmpMicrobe[idx] = microbe[idx];
				q.push({ r,c });
			}
			else
			{
				if (microbe[board[r][c]] < microbe[idx])
				{
					tmpMicrobe[idx] += tmpMicrobe[board[r][c]];
					board[r][c] = idx;
				}
				else
				{
					tmpMicrobe[board[r][c]] += tmpMicrobe[idx];
				}
			}
		}
	}
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		init();
		input();
		bfs();

		printf("#%d %d\n", test_case, remainCnt);
	}

	return 0;
}