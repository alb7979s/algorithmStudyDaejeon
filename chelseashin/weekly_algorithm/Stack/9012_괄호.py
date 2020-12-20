import sys
sys.stdin = open("9012_input.txt")
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    temp = list(input().strip())
    # print(len(temp), temp)
    stack = []
    for t in temp:
        if not stack:
            stack.append(t)
        else:   # 스택에 값 있을 때
            if stack[-1] == "(" and t == ")":
                stack.pop()
            else:
                stack.append(t)
    if not len(stack):
        print("YES")
    else:
        print("NO")