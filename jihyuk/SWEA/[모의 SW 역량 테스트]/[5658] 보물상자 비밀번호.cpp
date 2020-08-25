#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

const int MAX = 28;

int T;
int N, K;
int Q;
vector<int> result;
char buffer[MAX + 1];
int number[MAX];

void decode()
{
	for (int i = 0; i < N; i++)
	{
		number[i] = buffer[i] <= '9' ? buffer[i] - '0' : buffer[i] - 'A' + 10;
	}
}

void rotate(int n)
{
	int num[4] = { 0 };
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < Q; j++)
		{
			int idx = (n + j + Q * i) % N;
			num[i] += (1 << ((Q - j - 1) * 4)) * number[idx];
		}

		result.push_back(num[i]);
	}
}

int main(int argc, char** argv)
{
	scanf("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		scanf("%d %d", &N, &K);
		Q = N >> 2;

		scanf("%s", buffer);
		decode();

		result.clear();

		for (int j = 0; j < Q; j++)
		{
			rotate(j);
		}

		sort(result.begin(), result.end(), greater<int>());
		result.erase(unique(result.begin(), result.end()), result.end());

		printf("#%d %d\n", i, result[K-1]);
	}

	return 0;
}