#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool checkCorrect(string& str)
{
    int pos = 0;
    int top = 0;
    while (pos < str.size())
    {
        if ('(' == str[pos])
        {
            top++;
        }
        else
        {
            if (!top)
            {
                return false;
            }
            top--;
        }
        pos++;
    }

    return true;
}

string parse(const string& str)
{
    int pos = 0;
    if (0 == str.size())
    {
        return "";
    }

    int lCnt = 0, rCnt = 0;
    '(' == str[pos++] ? lCnt++ : rCnt++;

    while (lCnt != rCnt)
    {
        '(' == str[pos++] ? lCnt++ : rCnt++;
    }

    string u = str.substr(0, pos);
    string v = parse(str.substr(pos, str.size()));

    if (checkCorrect(u))
    {
        return u + v;
    }
    else
    {
        for (size_t i = 1; i < u.size() - 1; i++)
        {
            '(' == u[i] ? u[i] = ')' : u[i] = '(';
        }
        string tmpStr = "(" + v + ")" + u.substr(1, u.size() - 2);
        return tmpStr;
    }
}

string solution(string str)
{
    return parse(str);
}

int main()
{
    string str;
    cin >> str;

    cout << solution(str);

    return 0;
}
