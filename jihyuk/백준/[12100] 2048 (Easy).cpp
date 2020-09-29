#include <cstdio>
#include <algorithm>
#include <memory.h>

using namespace std;

int N;
int board[20][20];
int result = 0;
int dx[4] = { 1, -1, 1, -1 };
int startIdx[4] = { 0 };

void moveBlock(int dir)
{
	int q[20];
	int s = 0, e = 0;

	for (int i = 0; i < N; i++)
	{
		s = e = 0;
		bool mergable = false;

		int j = startIdx[dir];

		while (0 <= j && j < N)
		{
			int& val = dir & 2 ? board[i][j] : board[j][i];
			if (val)
			{
				if (mergable && q[e - 1] == val)
				{
					mergable = false;
					q[e - 1] <<= 1;
					val = 0;
				}
				else
				{
					mergable = true;
					q[e++] = val;
					val = 0;
				}
			}

			j += dx[dir];
		}

		j = startIdx[dir];

		while (s != e)
		{
			int& val = dir & 2 ? board[i][j] : board[j][i];
			val = q[s++];
			j += dx[dir];
		}
	}
}

void solve(int k)
{
	if (k == 5)
	{
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				result = max(result, board[i][j]);

		return;
	}

	int restore[20][20];
	memcpy(restore, board, sizeof(board));

	for (int i = 0; i < 4; i++)
	{
		moveBlock(i);
		solve(k + 1);
		memcpy(board, restore, sizeof(board));
	}
}

int main()
{
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &board[i][j]);
		}
	}

	for (int i = 0; i < 4; i++)
	{
		startIdx[i] = 0 == (i & 1) ? 0 : N - 1;
	}


	solve(0);
	printf("%d", result);
}