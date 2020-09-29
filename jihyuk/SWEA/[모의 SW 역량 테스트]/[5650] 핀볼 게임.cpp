#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

const int BLACK_HOLE = -1;
const int UP = 0;
const int RIGHT = 1;
const int DOWN = 2;
const int LEFT = 3;

int result;
int curSocre;
int N;
int dr[4] = { -1, 0, 1, 0 }; // 상우하좌
int dc[4] = { 0, 1, 0, -1 };
int block[6][4] =
{   {0,0,0,0},
    {DOWN, LEFT, RIGHT, UP},
    {RIGHT, LEFT, UP, DOWN},
    {LEFT, DOWN, UP, RIGHT},
    {DOWN, UP, LEFT, RIGHT},
    {DOWN, LEFT, UP, RIGHT}
};
int board[100][100];
map<pair<int, int>, pair<int, int>> wormhole;
pair<int, int> pos;
pair<int, int> start;
int dir;

void init()
{
    result = curSocre = 0;
    wormhole.clear();
}

bool isIn(int r, int c)
{
    return 0 <= r && r < N && 0 <= c && c < N;
}

void input()
{
    scanf("%d", &N);

    map<int, vector<pair<int,int>>> m;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &board[i][j]);
            if (6 <= board[i][j])
            {
                m[board[i][j]].push_back({ i,j });
            }
        }
    }

    for (auto& it : m)
    {
        int r0, c0, r1, c1;
        r0 = it.second[0].first;
        c0 = it.second[0].second;
        r1 = it.second[1].first;
        c1 = it.second[1].second;

        wormhole[{r0, c0}] = { r1, c1 };
        wormhole[{r1, c1}] = { r0, c0 };
    }
}

void move()
{
    int nr = pos.first + dr[dir];
    int nc = pos.second + dc[dir];
    if (false == isIn(nr, nc))
    {
        dir = (dir + 2) % 4;
        curSocre++;
    }
    else if (1 <= board[nr][nc] && board[nr][nc] <= 5)
    {
        dir = block[board[nr][nc]][dir];
        curSocre++;
    }
    else if (6 <= board[nr][nc])
    {
        pos = wormhole[{nr, nc}];
        return;
    }

    pos.first = nr;
    pos.second = nc;
}

void simulate()
{
    curSocre = 0;
    move();
    int val = board[pos.first][pos.second];

    while (-1 != val && start != pos)
    {
        move();
        if (isIn(pos.first, pos.second))
        {
            val = board[pos.first][pos.second];
        }
    }
    result = max(result, curSocre);
}

void solve()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (0 == board[i][j])
            {
                for (int k = 0; k < 4; k++)
                {
                    dir = k;
                    int nr = i + dr[dir];
                    int nc = j + dc[dir];
                    if (isIn(nr, nc) && board[nr][nc] == board[i][j])
                    {
                        continue;
                    }
                    start = pos = { i, j };
                    simulate();
                }
            }
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
