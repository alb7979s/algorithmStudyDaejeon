#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

vector<int> numbers;
vector<int> op;
vector<int> order;
int priority[3];
stack<long long> numStack;
stack<int> opStack;

void token(string& expression)
{
	int num = 0;
	char ch;
	bool checkOp[3] = { false };

	for (size_t i = 0; i < expression.size(); i++)
	{
		ch = expression[i];
		switch (ch)
		{
		case '+':
			op.push_back(0);
			numbers.push_back(num);
			if (false == checkOp[0])
			{
				order.push_back(0);
				checkOp[0] = true;
			}

			num = 0;
			break;
		case '-':
			op.push_back(1);
			numbers.push_back(num);
			if (false == checkOp[1])
			{
				order.push_back(1);
				checkOp[1] = true;
			}
			num = 0;
			break;
		case '*':
			op.push_back(2);
			numbers.push_back(num);
			if (false == checkOp[2])
			{
				order.push_back(2);
				checkOp[2] = true;
			}
			num = 0;
			break;
		default:
			num = num * 10 + expression[i] - '0';
			break;
		}
	}
	numbers.push_back(num);
	std::sort(order.begin(), order.end());
}

void calc()
{
	int op = opStack.top();
	opStack.pop();

	long long n2 = numStack.top();
	numStack.pop();

	long long n1 = numStack.top();
	numStack.pop();

	switch (op)
	{
	case 0:
		numStack.push(n1 + n2);
		break;
	case 1:
		numStack.push(n1 - n2);
		break;
	case 2:
		numStack.push(n1 * n2);
		break;
	}
}

long long solution(string expression)
{
	long long answer = 0;

	numbers.reserve(expression.size());
	op.reserve(expression.size() - 1);

	token(expression);

	do
	{
		numStack = stack<long long>();
		opStack = stack<int>();

		numStack.push(numbers[0]);
		for (size_t i = 0; i < order.size(); i++)
		{
			priority[order[i]] = order.size() - i;
		}
		for (int i = 0; i < op.size(); i++)
		{
			while (!opStack.empty() && priority[op[i]] <= priority[opStack.top()])
				calc();
			opStack.push(op[i]);
			numStack.push(numbers[i + 1]);
		}

		while (!opStack.empty())
			calc();

		answer = max(answer, abs(numStack.top()));

	} while (next_permutation(order.begin(), order.end()));

	return answer;
}
/*
int main()
{
	string expression;
	cin >> expression;

	cout << solution(expression);

	return 0;
}
*/