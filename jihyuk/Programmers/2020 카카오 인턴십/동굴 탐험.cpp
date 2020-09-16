#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

const int MAX = 200000;

vector<vector<int>> edge; // undirected edge
vector<int> key;
bool needKey[MAX];
bool visited[MAX];
int N;

void bfs()
{
    queue<int> q;
    q.push(0);
    visited[0] = true;
    if (needKey[0])
    {
        return;
    }

    set<int> s;

    while (!q.empty())
    {
        int idx = q.front();
        q.pop();
        needKey[key[idx]] = false;

        if (s.find(key[idx]) != s.end())
        {
            s.erase(key[idx]);
            visited[key[idx]] = true;
            q.push(key[idx]);
        }

        for (const auto& e : edge[idx])
        {
            if (visited[e])
                continue;

            if (needKey[e])
            {
                s.insert(e);
                continue;
            }

            visited[e] = true;
            q.push(e);
        }
    }
}

bool solution(int n, vector<vector<int>> path, vector<vector<int>> order)
{
    N = n;

    edge.resize(N);
    for (auto& e : path)
    {
        edge[e[0]].push_back(e[1]);
        edge[e[1]].push_back(e[0]);
    }

    key.resize(N, 0);
    for (auto& e : order)
    {
        key[e[0]] = e[1];
        needKey[e[1]] = true;
    }
    
    bfs();

    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int n, m;
    cin >> n >> m;

    vector<vector<int>> path, order;
    path.resize(n - 1, vector<int>(2, 0));
    order.resize(m, vector<int>(2, 0));

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin >> path[i][j];
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin >> order[i][j];
        }
    }

    cout << solution(n, path, order);

    return 0;
}
