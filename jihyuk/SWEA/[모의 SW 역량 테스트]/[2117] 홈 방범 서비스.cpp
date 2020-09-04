#include<cstdio>
#include<algorithm>
#include<queue>
#include<memory.h>

using namespace std;

int N, M;
int board[20][20];
int totalCost;
int maxCnt;

void init()
{
	memset(board, 0, sizeof(board));
	maxCnt = 0;
}

void input()
{
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &board[i][j]);
		}
	}
}

bool calc(int r, int c, int k)
{
	int cnt = 0;
	int cost = totalCost;

	int start = c;
	int end = c + 1;

	for (int i = r - k + 1; i <= r; i++, start--, end++)
	{
		if (i < 0)
		{
			continue;
		}

		for (int j = start; j < end; j++)
		{
			if (j < 0)
			{
				continue;
			}
			else if (N <= j)
			{
				break;
			}

			if (board[i][j])
			{
				cnt++;
			}
		}
	}

	start = c;
	end = c + 1;
	for (int i = r + k - 1; r < i; i--, start--, end++)
	{
		if (N <= i)
		{
			continue;
		}

		for (int j = start; j < end; j++)
		{
			if (j < 0)
			{
				continue;
			}
			else if (N <= j)
			{
				break;
			}

			if (board[i][j])
			{
				cnt++;
			}
		}
	}

	cost = cnt * M;
	if (totalCost <= cost && maxCnt < cnt)
	{
		maxCnt = cnt;
	}

	return totalCost <= cost;
}

void solve()
{
	int k = N & 1 ? N : N + 1;
	bool flag;

	while (k)
	{
		maxCnt = 0;
		totalCost = k * k + (k - 1) * (k - 1);
		flag = false;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (calc(i, j, k))
				{
					flag = true;
				}
			}
		}

		if (flag)
		{
			return;
		}

		k--;
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
		solve();

		printf("#%d %d\n", test_case, maxCnt);
	}

	return 0;
}