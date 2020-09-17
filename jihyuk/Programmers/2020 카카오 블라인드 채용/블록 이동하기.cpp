#include<string>
#include<vector>
#include<algorithm>
#include<iostream>
#include<queue>

using namespace std;

struct RobotInfo
{
    RobotInfo(int r, int c, int dir) : r(r), c(c), dir(dir) {}
    int r, c;
    int dir; // 0 수평방향, 1 수직 방향
};

int N;
int dr[4] = { -1, 1, 0, 0 }; // 상하 좌우
int dc[4] = { 0, 0, -1, 1 }; // 상하 좌우
int dr2[2] = { 0, 1 };
int dc2[2] = { 1, 0 };
int board[100][100][2];
int timeBoard[100][100][2];
int rot[2][4][2] =
{
    // 수평 방향일 때
    {
        { -1, 0},
        { 0, 0},
        { -1, 1},
        { 0, 1},
        /*{ -1, 0, 0 ,-1},
        { 0, 0, 1, -1},
        { -1, 1, 0, 0},
        { 0, 1, 1, 0},*/
    }
    ,
    // 수직 방향일 때
    {
        { 0, -1},
        { 0, 0},
        { 1, -1},
        { 1, 0},
        /*{ 0, -1, -1 ,0},
        { 0, 0, -1, 1},
        { 1, -1, 0, 0},
        { 1, 0, 0, 1},*/
    }
};
int rotCheck[2][4][2] =
{
    {
        {-1, 1},
        {1, 1},
        {-1, 0},
        {1, 0},
    },
    {
        {1, -1},
        {1, 1},
        {0, -1},
        {0, 1},
    }
};

bool checkDest(int r, int c, int dir)
{
    if (r == N - 2 && c == N - 1 && dir == 1)
    {
        return true;
    }
    else if (r == N - 1 && c == N - 2 && dir == 0)
    {
        return true;
    }

    return false;
}

bool isIn(int r, int c)
{
    return 0 <= r && r < N && 0 <= c && c < N;
}

int bfs()
{
    queue<RobotInfo> q;
    q.push(RobotInfo(0, 0, 0));
    board[0][0][0] = 1;
    int time = 0;
    int qSize;

    while (!q.empty())
    {
        qSize = q.size();
        for (int i = 0; i < qSize; i++)
        {
            int r = q.front().r;
            int c = q.front().c;
            int dir = q.front().dir;
            q.pop();

            if (checkDest(r, c, dir))
            {
                return timeBoard[r][c][dir];
            }

            for (int moveDir = 0; moveDir < 4; moveDir++)
            {
                int nr = r + dr[moveDir];
                int nc = c + dc[moveDir];

                int nr2 = nr + dr2[dir];
                int nc2 = nc + dc2[dir];

                if (!isIn(nr, nc) || 0 != board[nr][nc][dir] || 
                    !isIn(nr2, nc2) || -1 == board[nr2][nc2][dir])
                {
                    continue;
                }

                timeBoard[nr][nc][dir] = timeBoard[r][c][dir] + 1;
                board[nr][nc][dir] = 1;
                q.push({ nr, nc, dir });
            }

            int nDir = (dir + 1) % 2;
            for (size_t i = 0; i < 4; i++)
            {
                int nr = r + rot[dir][i][0];
                int nc = c + rot[dir][i][1];

                int nr2 = nr + dr2[nDir];
                int nc2 = nc + dc2[nDir];

                int rotRow = r + rotCheck[dir][i][0];
                int rotCol = c + rotCheck[dir][i][1];

                if (!isIn(nr, nc) || 0 != board[nr][nc][nDir] || -1 == board[rotRow][rotCol][nDir]
                    || !isIn(nr2, nc2) || -1 == board[nr2][nc2][nDir])
                {
                    continue;
                }

                timeBoard[nr][nc][nDir] = timeBoard[r][c][dir] + 1;
                board[nr][nc][nDir] = 1;
                q.push({ nr, nc, nDir });
            }
        }
    }

    return time;
}

void init(vector<vector<int>>& raw)
{
    N = raw.size();
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            board[i][j][0] = board[i][j][1] = -raw[i][j];
        }
    }
}

int solution(vector<vector<int>> raw)
{
    init(raw);
    return bfs();
}

int main()
{
    int N;
    cin >> N;
    
    vector<vector<int>> board;
    board.resize(N, vector<int>(N));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> board[i][j];
        }
    }
    
    cout << solution(board);
 
    return 0;
}
