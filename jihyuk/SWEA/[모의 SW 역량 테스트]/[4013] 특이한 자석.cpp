#include<cstdio>
#include<algorithm>

using namespace std;

const int magCnt = 4;

int K;
int result;
unsigned char magnet[magCnt];

void init()
{
	result = 0;
}

void rotate(int n, int dir)
{
	if (1 == dir)
	{
		int flag = magnet[n] & (1 << 7) ? 1 : 0;
		magnet[n] = (magnet[n] << 1) + flag;
	}
	else
	{
		int flag = magnet[n] & 1 ? (1 << 7) : 0;
		magnet[n] = (magnet[n] >> 1) + flag;
	}
}

void input()
{
	scanf("%d", &K);
	
	for (int i = 0; i < magCnt; i++)
	{
		magnet[i] = 0;
		for (int j = 0; j < 8; j++)
		{
			int val;
			scanf("%d", &val);
			if (val)
			{
				magnet[i] |= 1 << j;
			}
		}
	}

	for (int i = 0; i < K; i++)
	{
		int n, dir;
		scanf("%d%d", &n, &dir);
		n--;
		int l = n, r = n;
		int lCnt = 0;
		int rCnt = 0;

		for (int i = l; 0 < i; i--)
		{
			if ((1 & ((magnet[i - 1] >> 2) ^ (magnet[i] >> 6)))) lCnt++;
			else break;
		}
		for (int i = n; 0 < magCnt - 1; i++)
		{
			if ((1 & ((magnet[i] >> 2) ^ (magnet[i + 1] >> 6)))) rCnt++;
			else break;
		}
		dir = ((n - lCnt) & 1) == (n & 1) ? dir : -dir;
		for (size_t i = n - lCnt; i <= n + rCnt; i++)
		{
			rotate(i, dir);
			dir = -dir;
		}
	}
}

void solve()
{
	for (int i = 0; i < magCnt; i++)
	{
		if (magnet[i] & 1)
		{
			result |= (1 << i);
		}
	}
}

int main(int argc, char** argv)
{
    int T;
	scanf("%d", &T);

	for (int test_case = 1; test_case <= T; ++test_case)
	{
		init();
		input();
		solve();

		printf("#%d %d\n", test_case, result);
	}

    return 0;
}
