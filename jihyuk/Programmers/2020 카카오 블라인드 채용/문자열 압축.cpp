#include <string>
#include <vector>
using namespace std;

int solution(string s)
{
    int len = s.length();
    int answer = len;

    for (int i = 1; i <= len / 2; i++)
    {
        int count = 1;
        string comp = s.substr(0, i);
        string result, cur;

        for (int j = i; j < len; j += i)
        {
            cur = s.substr(j, i);

            if (0 == comp.compare(cur))
                count++;
            else
            {
                if (1 == count)
                {
                    result += comp;
                    comp = cur;
                }
                else
                {
                    result += to_string(count) + comp;
                    comp = cur;
                    count = 1;
                }
            }

            if (j + i >= len)
            {
                1 < count ? result += to_string(count) + comp : result += s.substr(j);
                break;
            }
        }
        if (result.length() < answer)
            answer = result.length();
    }

    return answer;
}