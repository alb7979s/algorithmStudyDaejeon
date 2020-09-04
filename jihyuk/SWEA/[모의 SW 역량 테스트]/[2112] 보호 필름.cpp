#include<cstdio>
#include<algorithm>
#include<queue>
#include<memory.h>

using namespace std;

int D, W, K;
int raw[13][20];
int cell[13][20];
bool selected[13];
int minCnt;

void init()
{
	//memset(raw, 0, sizeof(raw));
	//memset(cell, 0, sizeof(cell));
	memset(selected, 0, sizeof(selected));
	minCnt = 987654321;
}

void input()
{
	scanf("%d%d%d", &D, &W, &K);
	for (int i = 0; i < D; i++)
	{
		for (int j = 0; j < W; j++)
		{
			scanf("%d", &raw[i][j]);
		}
	}
	memcpy(cell, raw, sizeof(raw));
}

bool checkValid()
{
	int cnt;
	int cmp;
	for (int width = 0; width < W; width++)
	{
		cmp = cell[0][width];
		cnt = 1;
		for (int depth = 1; depth < D; depth++)
		{
			if (cell[depth][width] == cmp)
			{
				cnt++;
			}
			else
			{
				cnt = 1;
				cmp = cell[depth][width];
			}

			if (K == cnt)
			{
				break;
			}
		}

		if (cnt < K)
		{
			return false;
		}
	}

	return true;
}

void inject(int depth, int drug)
{
	for (int i = 0; i < W; i++)
	{
		cell[depth][i] = drug;
	}
}

void recover(int depth)
{
	memcpy(&cell[depth][0], &raw[depth][0], sizeof(int) * W);
}

void dfs(int idx, int cnt)
{
	if (minCnt <= cnt)
	{
		return;
	}
	
	if (checkValid())
	{
		minCnt = min(minCnt, cnt);
		return;
	}

	for (int i = idx; i < D; i++)
	{
		if (true == selected[i])
		{
			continue;
		}
		selected[i] = true;
		
		// 약품 A 투여
		inject(i, 0);
		dfs(i, cnt + 1);

		// 약품 B 투여
		inject(i, 1);
		dfs(i, cnt + 1);

		recover(i);
		selected[i] = false;
	}
}

void solve()
{
	dfs(0, 0);
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

		printf("#%d %d\n", test_case, minCnt);
	}

	return 0;
}