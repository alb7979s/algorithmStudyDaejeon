#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

const int INF = 987654321;

int R, C;
int minTIme = INF;
char raw[50][50];
int dir[4][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
int dist[50][50];

queue<pair<int, int>> q;

void bfs()
{
	int r, c, r1, c1;

	while (!q.empty())
	{
		r = q.front().first, c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			r1 = r + dir[i][0], c1 = c + dir[i][1];

			if (r1 < 0 || R <= r1 || c1 < 0 || C <= c1 || -1 < dist[r1][c1])
			{
				continue;
			}
			else if ('D' == raw[r1][c1])
			{
				if ('S' == raw[r][c])
				{
					minTIme = dist[r][c] + 1;
					return;
				}
				else
				{
					continue;
				}
			}

			q.push({ r1, c1 });
			raw[r1][c1] = raw[r][c];
			dist[r1][c1] = dist[r][c] + 1;
		}
	}
}

void input()
{
	fill(&dist[0][0], (&dist[49][49]) + 1, -1);

	char str[51];
	pair<int, int> startPos;
	for (int i = 0; i < R; i++)
	{
		scanf("%s", str);
		for (int j = 0; j < C; j++)
		{
			raw[i][j] = str[j];
			if (raw[i][j] == 'S')
			{
				startPos = { i,j };
				dist[i][j] = 0;
			}
			else if (raw[i][j] == '*')
			{
				q.push({ i,j });
				dist[i][j] = 0;
			}
			else if (raw[i][j] == 'X')
			{
				dist[i][j] = 0;
			}
		}
	}
	q.push(startPos);
}

int main()
{
	scanf("%d %d", &R, &C);

	input();
	bfs();

	if (INF == minTIme)
	{
		printf("KAKTUS\n");
	}
	else
	{
		printf("%d\n", minTIme);
	}
}