#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int N, M, K, result = 987654321;
int raw[51][51];
int dup[51][51];
bool visited[6];
int op[6][3];
vector<int> pick;
int dir[4][2] = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };

void calculate()
{
	int sum;
	for (int i = 0; i < N; i++)
	{
		sum = 0;
		for (int j = 0; j < M; j++)
		{
			sum += dup[i][j];
		}
		if (sum < result)
		{
			result = sum;
		}
	}
}

void rotate()
{
	for (int n = 0; n < K; n++)
	{
		int r = op[pick[n]][0], c = op[pick[n]][1], s = op[pick[n]][2];
		
		for (int i = 1; i <= s; i++)
		{
			int tmp = dup[r - i][c - i];
			int row = r - i;
			int col = c - i;
			int size = 2 * i;

			for (int dirIdx = 0; dirIdx < 4; dirIdx++)
			{
				for (int i = 0; i < size; i++)
				{
					dup[row][col] = dup[row + dir[dirIdx][0]][col + dir[dirIdx][1]];
					row += dir[dirIdx][0];
					col += dir[dirIdx][1];
				}
			}
			dup[r - i][c - i + 1] = tmp;
		}
	}
}

void solve(int n)
{
	if (K == n)
	{
		copy(&raw[0][0], &raw[0][0] + 51 * 51, &dup[0][0]);
		rotate();
		calculate();
		return;
	}

	for (int i = 0; i < K; i++)
	{
		if (visited[i])
		{
			continue;
		}
		visited[i] = true;
		pick.push_back(i);
		solve(n + 1);
		visited[i] = false;
		pick.pop_back();
	}
}

int main()
{
	scanf("%d %d %d", &N, &M, &K);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			scanf("%d", &raw[i][j]);
		}
	}

	pick.reserve(K);
	
	for(int i = 0; i < K; i++)
	{
		scanf("%d %d %d", &op[i][0], &op[i][1], &op[i][2]);
		op[i][0]--, op[i][1]--;
	}

	solve(0);
	printf("%d", result);
}