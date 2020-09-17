#include<string>
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

int totalCnt;
int keySize;
int boardSize;

void rotate(vector<vector<int>>& key)
{
    vector<vector<int>> tmp(keySize, vector<int>(keySize));

    for (int i = 0; i < keySize; i++)
    {
        for (int j = 0; j < keySize; j++)
        {
            tmp[j][keySize - i - 1] = key[i][j];
        }
    }

    key = tmp;
}

bool unlock(int r, int c, vector<vector<int>>& key, vector<vector<int>> board)
{
    for (int i = r; i < r + keySize; i++)
    {
        for (int j = c; j < c + keySize; j++)
        {
            board[i][j] += key[i - r][j - c];
        }
    }

    for (int i = keySize - 1; i <= boardSize - keySize; i++)
    {
        for (int j = keySize - 1; j <= boardSize - keySize; j++)
        {
            if (board[i][j] != 1) // 자물쇠 영여이 홈끼리 부딪히거나, 채워져 있지 않은 경우 열 수 없다.
                return false;
        }
    }

    return true;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock)
{
    for (size_t i = 0; i < lock.size(); i++)
    {
        for (size_t j = 0; j < lock.size(); j++)
        {
            if (lock[i][j])
            {
                totalCnt++;
            }
        }
    }

    keySize = key.size();
    boardSize = lock.size() + 2 * (key.size() - 1);

    vector<vector<int>> board(boardSize, vector<int>(boardSize, 0));
    for (int i = keySize - 1; i <= boardSize - keySize; i++)
    {
        for (int j = keySize - 1; j <= boardSize - keySize; j++)
        {
            board[i][j] = lock[i - keySize + 1][j - keySize + 1];
        }
    }

	for (int i = 0; i < 4; i++)
	{
        for (int r = 0; r <= boardSize - keySize; r++)
        {
            for (int c = 0; c <= boardSize - keySize; c++)
            {
                if (unlock(r, c, key, board))
                    return true;
            }
        }

        if (i == 3)
            break;

        rotate(key);
	}

    return false;
}

int main()
{
    int N, M;
    cin >> N >> M;
    vector<vector<int>> key, lock;
    key = vector<vector<int>>(N, vector<int>(N));
    lock = vector<vector<int>>(M, vector<int>(M));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> key[i][j];
        }
    }
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> lock[i][j];
        }
    }

    cout << solution(key, lock);

    return 0;
}