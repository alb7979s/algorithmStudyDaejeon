#include<cstdio>
#include<algorithm>

using namespace std;

const int M = 4001;

int result;
int restCnt;
int N;

struct ATOM
{
    int x, y, d, k;
};

ATOM atom[1000];
int board[M][M];
bool isCollision[M][M];

void init()
{
    result = 0;
}

bool isIn(int r, int c)
{
    return 0 <= r && r < M && 0 <= c && c < M;
}

void input()
{
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {

        scanf("%d%d%d%d", &atom[i].x, &atom[i].y, &atom[i].d, &atom[i].k);
        atom[i].x = 2 * (atom[i].x + 1000);
        atom[i].y = 2 * (atom[i].y + 1000);
        board[atom[i].x][atom[i].y] = 1;
    }
}

void remove_atom(int idx)
{
    atom[idx] = atom[--restCnt];
}

void solve()
{
    restCnt = N;
    while(restCnt)
    {
        for (int i = 0; i < restCnt; i++)
        {
            int& x = atom[i].x;
            int& y = atom[i].y;
            int d = atom[i].d;
            board[x][y]--;

            if (0 == d) y++;
            else if (1 == d) y--;
            else if (2 == d) x--;
            else x++;

            if (!isIn(x, y))
            {
                atom[i] = atom[--restCnt];
                i--;
            }
            else
            {
                board[x][y]++;
                if (1 < board[x][y])
                {
                    isCollision[x][y] = true;
                }
            }
        }

        for (int i = 0; i < restCnt; i++)
        {
            int x = atom[i].x;
            int y = atom[i].y;

            if (isCollision[x][y])
            {
                board[x][y]--;
                if (0 == board[x][y])
                    isCollision[x][y] = false;

                result += atom[i].k;
                remove_atom(i);
                i--;
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