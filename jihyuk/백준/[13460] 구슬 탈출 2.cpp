#include<iostream>
#include<queue>

using namespace std;

const int MAX = 10;
const int R = 0;
const int B = 1;

int N, M;
char board[MAX][MAX];
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
bool visit[10][10][10][10];

struct MARBLE
{
	int r[2];
	int c[2];
};
queue<MARBLE> q;

void input()
{
	pair<int, int> r;
	pair<int, int> b;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> board[i][j];

			if ('R' == board[i][j])
			{
				r = { i, j };
				board[i][j] = '.';
			}
			else if ('B' == board[i][j])
			{
				b = { i, j };
				board[i][j] = '.';
			}
		}
	}

	q.push({ r.first, b.first, r.second, b.second });
	visit[r.first][r.second][b.first][b.second] = true;
}

void move_marble(int& r, int& c, int &dist, int a, int b)
{
	while (board[r + a][c + b] != '#' && board[r][c] != 'O')
	{
		r += a;
		c += b;
		dist += 1;
	}
}

void solve()
{
	int time = 0;
	int dist[2] = { 0, 0};

	int r[2], c[2], nr[2], nc[2];

	while (!q.empty() && time < 10)
	{
		time++;

		int qSize = q.size();
		for (int i = 0; i < qSize; i++)
		{
			r[R] = q.front().r[R], c[R] = q.front().c[R];
			r[B] = q.front().r[B], c[B] = q.front().c[B];
			q.pop();

			for (int dir = 0; dir < 4; dir++)
			{
				nr[R] = r[R], nc[R] = c[R];
				nr[B] = r[B], nc[B] = c[B];

				dist[R] = dist[B] = 0;
				move_marble(nr[R], nc[R], dist[R], dr[dir], dc[dir]);
				move_marble(nr[B], nc[B], dist[B], dr[dir], dc[dir]);

				if ('O' == board[nr[B]][nc[B]]) continue;
				if ('O' == board[nr[R]][nc[R]])
				{
					cout << time;
					return;
				}

				if (nr[R] == nr[B] && nc[R] == nc[B])
				{
					if (dist[B] < dist[R]) nr[R] -= dr[dir], nc[R] -= dc[dir];
					else nr[B] -= dr[dir], nc[B] -= dc[dir];
				}

				if (visit[nr[R]][nc[R]][nr[B]][nc[B]])
					continue;

				visit[nr[R]][nc[R]][nr[B]][nc[B]] = true;
				q.push({ nr[R], nr[B], nc[R], nc[B] });
			}
		}
	}

	printf("-1");
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> M;
	input();
	solve();

}