#include<string>
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

bool board[101][101][2];
int totalCnt;
int N;

bool check(int x, int y, int t)
{
    // 기둥 설치
    if (0 == t)
    {
        // 바닥 위에 있거나, 보의 한쪽 끝에 있거나, 다른 기둥 위 에 있거나
        if (y == 0 || ( (0 < x && board[x - 1][y][1]) || board[x][y][1] ) || board[x][y - 1][0])
        {
            return true;
        }
    }
    // 보 설치
    else
    {
        // 한 쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나
        if ((board[x][y - 1][0] || (x < N && board[x + 1][y - 1][0])) ||
            (0 < x && x < N && board[x - 1][y][1] && board[x + 1][y][1]))
        {
            return true;
        }
    }

    return false;
}

void install(int x, int y, int t)
{
    if (check(x, y, t))
    {
        board[x][y][t] = true;
    }
}

void erase(int x, int y, int t)
{
    board[x][y][t] = false;

    bool erasable = true;

    if (0 == t) // 기둥 삭제
    {
        // case 1 : 위에 기둥이 있을 때
        // case 2, 3 : 기둥 위에 보가 있는 경우 (보의 왼쪽 부분이 걸친 경우, 오른쪽 부분이 걸친 경우)
        if (board[x][y + 1][0] && !check(x, y + 1, 0))
        {
            erasable = false;
        }
        else if(board[x][y + 1][1] && !check(x, y + 1, 1))
        {
            erasable = false;
        }
        else if (0 < x && board[x - 1][y + 1][1] && !check(x - 1, y + 1, 1))
        {
            erasable = false;
        }
    }
    else
    {
        // case 1,2 : 기둥이 보의 한쪽 끝에 걸친 경우
        // case 3,4 : 좌, 우에 있는 보가 있는 경우 
        if (board[x][y][0] && !check(x, y, 0)) // 보의 위치에 기둥이 있는 경우
        {
            erasable = false;
        }
        else if (x < N && board[x + 1][y][0] && !check(x + 1, y, 0)) // 보가 뻗친 오른쪽 끝에 기둥이 있는 경우
        {
            erasable = false;
        }
        else if (0 < x && board[x - 1][y][1] && !check(x - 1, y, 1)) // 왼쪽에 보가 있는 경우
        {
            erasable = false;
        }
        else if (x < N && board[x + 1][y][1] && !check(x + 1, y, 1)) // 오른쪽에 보가 있는 경우
        {
            erasable = false;
        }
    }

    board[x][y][t] = !erasable;
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame)
{
    vector<vector<int>> answer;
    N = n;
    
    for (size_t i = 0; i < build_frame.size(); i++)
    {
        int x = build_frame[i][0];
        int y = build_frame[i][1];
        int a = build_frame[i][2];
        int b = build_frame[i][3];

        b ? install(x, y, a) : erase(x, y, a);
    }

    answer.reserve(totalCnt);
    
    for (int x = 0; x < n + 1; x++)
    {
        for (int y = 0; y < n + 1; y++)
        {
            for (int t = 0; t < 2; t++)
            {
                if (board[x][y][t])
                {
                    answer.push_back({ x, y, t });
                }
            }
        }
    }

    return answer;
}


int main()
{
    int N, M;
    cin >> N >> M;
    
    vector<vector<int>> build_frame;
    build_frame.resize(M, vector<int>(4, 0));

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cin >> build_frame[i][j];
        }
    }

    vector<vector<int>> ret = solution(N, build_frame);
    for (size_t i = 0; i < ret.size(); i++)
    {
        for (size_t j = 0; j < ret[i].size(); j++)
        {
            cout << ret[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
