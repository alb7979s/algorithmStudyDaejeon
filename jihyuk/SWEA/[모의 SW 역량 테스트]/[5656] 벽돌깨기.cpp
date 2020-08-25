#include<cstdio>
#include<algorithm>
#include<memory.h>
#include<queue>

using namespace std;

int T, N, H, W;
int minRemainCnt;
int block[15][12];
int dir[4][2] = { {-1, 0}, {1, 0}, {0, 1}, {0, -1} };

bool isIn(int r, int c)
{
	return 0 <= r && r < H && 0 <= c && c < W;
}

void breakBlock(int dropCol)
{
	struct info
	{
		info(int r, int c, int n) : r(r), c(c), n(n) {};
		int r;
		int c;
		int n;
	};

	queue<info> q;

	for (int i = 0; i < H; i++)
	{
		if (0 < block[i][dropCol])
		{
			q.push({ i, dropCol, block[i][dropCol] });
			block[i][dropCol] = 0;
			break;
		}
	}
	
	while (!q.empty())
	{
		int r = q.front().r;
		int c = q.front().c;
		int n = q.front().n;

		q.pop();

		for (int idx = 0; idx < 4; idx++)
		{
			for (int i = 1; i < n; i++)
			{
				int dr = r + dir[idx][0] * i;
				int dc = c + dir[idx][1] * i;

				if (isIn(dr, dc) && 0 < block[dr][dc])
				{
					q.push({ dr, dc, block[dr][dc] });
					block[dr][dc] = 0;
				}
			}
		}
	}
}

void dropBlock()
{
	for (int i = 0; i < W; i++)
	{
		for (int j = H - 1, k = H - 2; 1 <= j; j--)
		{
			// 아래에서부터 검사했을 때, 깨진 블록인지 검사. 깨지지 않았으면 바로 위 행 다시 검사
			if (0 != block[j][i])
			{
				continue;
			}
			
			if (j <= k)
			{
				k = j - 1;
			}

			// 아래로 한칸 떨구기
			for (; 0 <= k; k--)
			{
				if (0 != block[k][i])
				{
					block[j][i] = block[k][i];
					block[k][i] = 0;
					break;
				}
			}
		}
	}
}

void backTrack(const int k)
{
	if (k == N)
	{
		int remainCnt = 0;

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				if (0 != block[i][j])
				{
					remainCnt++;
				}
			}
		}

		if (remainCnt < minRemainCnt)
		{
			minRemainCnt = remainCnt;
		}
		return;
	}

	int currentBlock[15][12] = { 0 };
	memcpy(currentBlock, block, 15 * 12 * sizeof(int));

	for (int i = 0; i < W; i++)
	{
		breakBlock(i); // 블록 제거
		dropBlock(); // 블록 정렬
		backTrack(k + 1); // 그 다음 횟수차로 다시 진행
		memcpy(block, currentBlock, 15 * 12 * sizeof(int)); // 이전 상태로 복원
	}
}

int main(int argc, char** argv)
{
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d%d%d", &N, &W, &H);

		minRemainCnt = 987654321;

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				scanf("%d", &block[i][j]);
			}
		}

		backTrack(0);

		printf("#%d %d\n", testCase, minRemainCnt);
	}

	return 0;
}