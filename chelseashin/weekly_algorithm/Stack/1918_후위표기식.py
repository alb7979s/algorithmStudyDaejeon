import sys
input = sys.stdin.readline
# S = "A+B*C"
S = "A+B*C-D/E"
# S = "(" + input() + ")"
S = "(" + S + ")"
# print(S)
priority = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
    "(": 0
}

stack = []
answer = ""
for t in S:
    if "A" <= t <= "Z":
        answer += t
    elif t == "(":
        stack.append(t)
    elif t == ")":
        while True:
            n = stack.pop()
            if n == "(":
                break
            answer += n
    else:   # 연산자일 경우
        while stack[-1] != "(" and priority[t] <= priority[stack[-1]]:
            answer += stack.pop()
        stack.append(t)
    # print(t, stack, answer)

print(answer)