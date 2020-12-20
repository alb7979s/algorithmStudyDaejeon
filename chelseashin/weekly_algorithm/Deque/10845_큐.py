import sys
sys.stdin = open("10845_input.txt")
from collections import deque
input = sys.stdin.readline

N = int(input())
Q = deque()
for _ in range(N):
    cmd = list(input().split())
    # print(cmd)
    if cmd[0] == "push":
        Q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(Q))
    elif cmd[0] == "empty":
        if Q:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if Q:
            print(Q[-1])
        else:
            print(-1)