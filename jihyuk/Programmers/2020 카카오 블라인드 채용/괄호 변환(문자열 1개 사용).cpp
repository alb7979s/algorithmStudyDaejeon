#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool checkCorrect(int pos, int end, string& str)
{
    int top = 0;
    while (pos < end)
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

void parse(int start, string& str)
{
    int pos = start;
    if (pos == str.size())
    {
        return;
    }

    int lCnt = 0, rCnt = 0;
    '(' == str[pos++] ? lCnt++ : rCnt++;

    while (lCnt != rCnt)
    {
        '(' == str[pos++] ? lCnt++ : rCnt++;
    }

    parse(pos, str);

    if (false == checkCorrect(start, pos, str)) // 올바른 문자열이 아닌 경우
    {
        int count = str.size() - start;
        for (int i = start + 1; i < pos - 1; i++)
        {
            '(' == str[i] ? str[i] = ')' : str[i] = '(';
        }

        string u = "(" + str.substr(pos, count) + ")" + str.substr(start + 1, pos - start - 2);
        str.replace(start, count, u.c_str());
    }
}

string solution(string str)
{
    parse(0, str);
    return str;
}

int main()
{
    string str;
    cin >> str;

    cout << solution(str);

    return 0;
}
