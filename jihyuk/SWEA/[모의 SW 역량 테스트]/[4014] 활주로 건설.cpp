#include<cstdio>
#include<algorithm>

using namespace std;

const int MAX = 20;

int N, X, result;
int board[2][MAX][MAX];

void init()
{
	result = 0;
}

void input()
{
	scanf("%d %d", &N, &X);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &board[0][i][j]);
			board[1][j][i] = board[0][i][j];
		}
	}
}
void solve()
{
    int prev = 0;
    int len = 0;

    for (int idx = 0; idx < 2; idx++)
    {
		for (int i = 0; i < N; i++)
		{
            len = 0;
            prev = board[idx][i][0];

            for (int j = 0; j < N; j++)
            {
                if (1 < abs(prev - board[idx][i][j])) // 높이차가 1보다 큰 경우
                {
                    break;
                }
                else if (prev == board[idx][i][j]) // 평지
                {
                    len++;
                }
                else if (prev < board[idx][i][j]) // 오르막
                {
                    if (len < X)
                        break;
                    len = 1;
                }
                else // 내리막
                {
                    if (len < 0)
                        break;
                    len = -X + 1;
                }

                prev = board[idx][i][j];
                if (j == N - 1)
                {
                    if (len < 0) break;
                    else result += 1;
                }
            }
		}
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

		printf("#%d %d\n", test_case, result);
	}

    return 0;
}
