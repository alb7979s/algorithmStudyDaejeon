import sys
sys.stdin = open("10828_input.txt")
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    cmd = list(input().split())
    # print(cmd)
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)