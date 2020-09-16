#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<pair<int, int>> keyPad;
int press[10];
pair<int, int> lHand;
pair<int, int> rHand;
bool isRHand;

void initKeyPad()
{
    keyPad.reserve(10);
    keyPad.push_back({ 3,1 });
    for (int i = 0; i <= 9; i++)
    {
        keyPad.push_back({ i / 3, i % 3 });
        press[i] = i % 3;
    }
    press[0] = 2;
    lHand = { 3, 0 };
    rHand = { 3, 2 };
}

string solution(vector<int> numbers, string hand)
{
    string answer = "";
    answer.reserve(numbers.size());
    isRHand = 0 == hand.compare("right");
    initKeyPad();

    int lDist, rDist;

    for (size_t i = 0; i < numbers.size(); i++)
    {
        int idx = numbers[i];
        if (0 == press[idx])
        {
            answer.push_back('R');
            rHand = keyPad[idx];
        }
        else if (1 == press[idx])
        {
            answer.push_back('L');
            lHand = keyPad[idx];
        }
        else
        {
            lDist = abs(lHand.first - keyPad[idx].first) + abs(lHand.second - keyPad[idx].second);
            rDist = abs(rHand.first - keyPad[idx].first) + abs(rHand.second - keyPad[idx].second);
            if (lDist == rDist)
            {
                if (isRHand)
                {
                    answer.push_back('R');
                    rHand = keyPad[idx];
                }
                else
                {
                    answer.push_back('L');
                    lHand = keyPad[idx];
                }
            }
            else if (lDist < rDist)
            {
                answer.push_back('L');
                lHand = keyPad[idx];
            }
            else
            {
                answer.push_back('R');
                rHand = keyPad[idx];
            }
        }
    }

    return answer;
}
/*
int main()
{
    vector<int> numbers;
    string hand;

    int N;
    cin >> N;
    numbers.resize(N, 0);
    for (int i = 0; i < N; i++)
    {
        cin >> numbers[i];
    }
    cin >> hand;

    cout << solution(numbers, hand);

    return 0;
}
*/