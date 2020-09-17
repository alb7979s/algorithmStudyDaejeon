
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
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
vector<vector<int>> dist;
int N;

struct Node
{
    Node(int r, int c, int cost, int dir) : r(r), c(c), cost(cost), dir(dir) {}
    int r, c;
    int cost;
    int dir;
};

struct comp
{
    bool operator()(const Node& l, const Node& r) {
        return l.cost < r.cost;
    }
};

int solution(vector<vector<int>> board)
{
    N = board.size();

    dist = vector<vector<int>>(N, vector<int>(N, INF));

    queue<Node> q;
    q.push(Node(0, 0, 0, 1));
    q.push(Node(0, 0, 0, 3));

    while (!q.empty())
    {
        int r = q.front().r;
        int c = q.front().c;
        int cost = q.front().cost;
        int dir = q.front().dir;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr < 0 || N <= nr || nc < 0 || N <= nc || board[nr][nc] == WALL)
                continue;

            if (dir == i)
            {
                int nCost = cost + 100;
                if (nCost <= dist[nr][nc])
                {
                    dist[nr][nc] = nCost;
                    q.push({ nr, nc, nCost, i });
                }
            }
            else
            {
                int nCost = cost + 600;
                if (nCost <= dist[nr][nc])
                {
                    dist[nr][nc] = nCost;
                    q.push({ nr, nc, nCost, i });
                }
            }
        }
    }

    return dist[N - 1][N - 1];
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