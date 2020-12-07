import sys
sys.stdin = open("1935_input.txt")
input = sys.stdin.readline

N = int(input())
S = list(input())
L = [int(input()) for _ in range(N)]
stack = []
for s in S:
    if 'A' <= s <= 'Z':
        stack.append(L[ord(s) - ord('A')])

    elif len(stack) >= 2:
        b = stack.pop()
        a = stack.pop()
        if s == "+":
            stack.append(a + b)
        elif s == "-":
            stack.append(a - b)
        elif s == "*":
            stack.append(a * b)
        else:
            stack.append(a / b)
print("%.2f" %stack[0])
