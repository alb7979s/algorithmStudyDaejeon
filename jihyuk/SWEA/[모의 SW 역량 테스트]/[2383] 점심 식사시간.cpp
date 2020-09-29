#include<cstdio>
#include<algorithm>
#include<queue>

using namespace std;

struct Person
{
	int r, c;
};
struct Stair
{
	int r, c, t;
};

int result;
int N;
int room[10][10];
Person p[10];
Stair s[2];
int pCnt;
int sCnt;
int pick[10];
int arrivedTime[2][10];

void init()
{
	result = 987654321;
	pCnt = 0;
	sCnt = 0;
}

void input()
{
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &room[i][j]);
			if (1 == room[i][j])
			{
				p[pCnt++] = { i, j };
			}
			else if (1 < room[i][j])
			{
				s[sCnt++] = { i,j, room[i][j] };
			}
		}
	}

	for (int i = 0; i < sCnt; i++)
	{
		for (int j = 0; j < pCnt; j++)
		{
			arrivedTime[i][j] = abs(s[i].r - p[j].r) + abs(s[i].c - p[j].c) + 1;
		}
	}
}

void caculate()
{
	int time = 0;
	int exitCnt = 0;

	queue<int> q[2];
	while (exitCnt < pCnt && time < result)
	{
		for (int i = 0; i < pCnt; i++)
		{
			if (arrivedTime[pick[i]][i] == time)
			{
				if (q[pick[i]].size() < 3)
				{
					q[pick[i]].push(s[pick[i]].t);
				}
				else
				{
					q[pick[i]].push(s[pick[i]].t + q[pick[i]].front());
				}
			}
		}

		for (int i = 0; i < 2; i++)
		{
			int qSize = q[i].size();
			for (int j = 0; j < qSize; j++)
			{
				int exitTime = q[i].front();
				q[i].pop();
				exitTime--;
				if (0 < exitTime)
				{
					q[i].push(exitTime);
				}
				else
				{
					exitCnt++;
				}
			}
		}
		time++;
	}

	result = min(result, time);
}

void selectStair(int n)
{
	if (n == pCnt)
	{
		caculate();
		return;
	}

	for (int i = 0; i < 2; i++)
	{
		pick[n] = i;
		selectStair(n + 1);
	}
}

void solve()
{
	selectStair(0);
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
