import sys
sys.stdin = open("2840_input.txt")

from collections import deque
N, K = map(int, input().split())
Q = deque(['?' for _ in range(N)])

visit = []
for i in range(K):
    num, char = map(str, input().split())
    # num만큼 시계방향 회전
    for j in range(int(num)):
        Q.appendleft(Q.pop())
    if Q[0] == char or (Q[0] == "?" and char not in visit):
        Q[0] = char
        visit.append(char)
    else:
        print("!")
        exit()
    print(int(num), Q, visit)

for _ in range(N):
    print(Q.popleft(), end = "")