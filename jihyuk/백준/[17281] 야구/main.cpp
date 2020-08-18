#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int N;
int outCnt;
int result;
int info[50][9];
vector<int> pick;
bool visited[9];
int order;
int base[3];

int play(int n)
{
	int sum = 0;
	while (outCnt < 3)
	{
		int value = info[n][pick[order++]];
		if (9 == order)
		{
			order = 0;
		}
		if (0 == value)
		{
			outCnt++;
			continue;
		}

		switch (value)
		{
		case 1:
			sum += base[2];
			base[2] = base[1];
			base[1] = base[0];
			base[0] = 1;
			break;
		case 2:
			sum += base[2] + base[1];
			base[2] = base[0];
			base[1] = 1;
			base[0] = 0;
			break;
		case 3:
			sum += base[2] + base[1] + base[0];
			base[2] = 1;
			base[0] = base[1] = 0;
			break;
		case 4:
			sum += base[2] + base[1] + base[0] + 1;
			base[0] = base[1] = base[2] = 0;
			break;
		}
	}

	return sum;
}

void playGame()
{
	order = 0;
	int sum = 0;
	
	for (int i = 0; i < N; i++)
	{
		outCnt = 0;
		base[0] = base[1] = base[2] = 0;
		sum += play(i);
	}

	if (result < sum)
	{
		result = sum;
	}
}

void choose(int n)
{
	if (0 == n)
	{
		swap(pick[0], pick[3]);
		playGame();
		swap(pick[0], pick[3]);
		return;
	}

	for (int i = 1; i < 9; i++)
	{
		if (visited[i])
		{
			continue;
		}

		pick.push_back(i);
		visited[i] = true;
		choose(n - 1);
		pick.pop_back();
		visited[i] = false;
	}
}

int main()
{
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			scanf("%d", &info[i][j]);
		}
	}

	pick.push_back(0);
	choose(8);

	printf("%d", result);
}