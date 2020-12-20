import sys
from collections import deque
sys.stdin = open("10866_input.txt")
input = sys.stdin.readline

N = int(input())
Q = deque()
for _ in range(N):
    cmd = list(input().split())
    # print(cmd)
    if cmd[0] == "push_front":
        Q.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        Q.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if Q:
            print(Q.pop())
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