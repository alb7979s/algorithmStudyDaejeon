#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

const int INF = 987654321;
const int WALL = 1;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
vector<vector<int>> cost[2];
int N;

struct Node
{
    Node(int r, int c, int type) : r(r), c(c), type(type) {}
    int r, c;
    int type;
};

struct comp
{
    bool operator()(const Node& lh, const Node& rh) {
        return cost[lh.type][lh.r][lh.c] > cost[rh.type][rh.r][rh.c];
    }
};

int solution(vector<vector<int>> board)
{
    N = board.size();

    cost[0] = vector<vector<int>>(N, vector<int>(N, INF));
    cost[1] = vector<vector<int>>(N, vector<int>(N, INF));

    priority_queue<Node, vector<Node>, comp> q;

    if (board[0][1] == 0)
    {
        cost[1][0][1] = 100;
        q.push({ 0, 1, 1 });
    }
    if (board[1][0] == 0)
    {
        cost[0][1][0] = 100;
        q.push({ 1, 0, 0 });
    }

    while (!q.empty())
    {
        int r = q.top().r;
        int c = q.top().c;
        int t = q.top().type;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nr = r + dr[i];
            int nc = c + dc[i];
            int nt = i >> 1;

            if (nr < 0 || N <= nr || nc < 0 || N <= nc || board[nr][nc] == WALL)
                continue;

            // 현재 노드에서 다음 노드로 이동할 때 드는 비용
            int newCost = cost[t][r][c] + (t == nt ? 100 : 600);

            // 현재 계산된 비용보다 기존에 계산된 비용이 같거나 작으면 갱신을 안한다.
            if (cost[nt][nr][nc] <= newCost) 
                continue;

            cost[nt][nr][nc] = newCost; // 현재 계산된 비용이 더 싼 경우 갱신
            q.push({ nr, nc, nt });
        }
    }

    return min(cost[0][N - 1][N - 1], cost[1][N - 1][N - 1]);
}
/*
int main()
{
    int N;
    cin >> N;
    vector<vector<int>> board;
    board.resize(N, vector<int>(N, 0));

    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            cin >> board[i][j];
        }
    }

    cout << solution(board);

    return 0;
}
*/