#include<cstdio>
#include<algorithm>
#include<map>
#include<memory.h>

using namespace std;

const int MAX = 10;
const int A = 0;
const int B = 1;

int dx[5] = { 0, 0, 1, 0, -1 }; // 상하좌우
int dy[5] = { 0, -1, 0, 1, 0 };

struct BC
{
	int idx;
	int p;
};

int maxSum;
int bc[8];
BC board[MAX][MAX][2]; // y, x, 1개 or 2개짜리
int path[2][101];
int totalMoveTime;
int cntBC;

void init()
{
	maxSum = 0;
	memset(board, 0, sizeof(board));
}

void input()
{
	scanf("%d%d", &totalMoveTime, &cntBC);
	for (int i = 0; i < 2; i++)
	{
		for (int j = 0; j < totalMoveTime; j++)
		{
			scanf("%d", &path[i][j]);
		}
	}
	
	for (int i = 0; i < cntBC; i++)
	{
		int r, c, range, performence;
		scanf("%d%d%d%d", &c, &r, &range, &performence);
		r--;
		c--;

		int startRow, endRow, startCol, endCol;

		startRow = r - range;
		endRow = r;
		
		startCol = c;
		endCol = c;

		for (int y = startRow; y <= endRow; y++, startCol--, endCol++)
		{
			if (y < 0)
			{
				continue;
			}
			for (int x = startCol; x <= endCol; x++)
			{
				if (x < 0 || MAX <= x)
				{
					continue;
				}

				if (board[y][x][0].p < performence)
				{
					board[y][x][1].p = board[y][x][0].p;
					board[y][x][1].idx = board[y][x][0].idx;

					board[y][x][0].p = performence;
					board[y][x][0].idx = i;
				}
				else if (board[y][x][1].p < performence)
				{
					board[y][x][1].p = performence;
					board[y][x][1].idx = i;
				}
			}
		}

		startRow = r + 1;
		endRow = r + range;

		startCol = c - (range - 1);
		endCol = c + (range - 1);
		for (int y = startRow; y <= endRow; y++, startCol++, endCol--)
		{
			if (MAX <= y)
			{
				continue;
			}
			for (int x = startCol; x <= endCol; x++)
			{
				if (x < 0 || MAX <= x)
				{
					continue;
				}

				if (board[y][x][0].p < performence)
				{
					board[y][x][1].p = board[y][x][0].p;
					board[y][x][1].idx = board[y][x][0].idx;

					board[y][x][0].p = performence;
					board[y][x][0].idx = i;
				}
				else if (board[y][x][1].p < performence)
				{
					board[y][x][1].p = performence;
					board[y][x][1].idx = i;
				}
			}
		}
	}
}

void solve()
{
	int Ax = 0, Ay = 0, Bx = MAX - 1, By = MAX - 1;
	
	for (int time = 0; time <= totalMoveTime; time++)
	{
		// Case1. 최대 충전할 수 있는 BC가 서로 다른 경우
		if (board[Ay][Ax][0].p != board[By][Bx][0].p)
		{
			maxSum += board[Ay][Ax][0].p + board[By][Bx][0].p;
		}
		//Case2.최대 충전할 수 있는 BC가 서로 같은 경우
		else if (0 < board[Ay][Ax][0].p && 0 < board[By][Bx][0].p 
			&& board[Ay][Ax][0].p == board[By][Bx][0].p)
		{
			if (board[Ay][Ax][0].idx == board[By][Bx][0].idx)
			{
				int a = board[Ay][Ax][0].p + board[By][Bx][1].p;
				int b = board[Ay][Ax][1].p + board[By][Bx][0].p;
				maxSum += max(a, b);
			}
			else
			{
				maxSum += board[Ay][Ax][0].p + board[By][Bx][0].p;
			}
		}

		Ax += dx[path[A][time]], Ay += dy[path[A][time]];
		Bx += dx[path[B][time]], By += dy[path[B][time]];
	}
}

int main(int main(int argc, char** argv))
{
    int T;
	scanf("%d", &T);

	for (int test_case = 1; test_case <= T; ++test_case)
	{
		init();
		input();
		solve();

		printf("#%d %d\n", test_case, maxSum);
	}

    return 0;
}
