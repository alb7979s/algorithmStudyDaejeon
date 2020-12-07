N = 5
P = [3, 2, 1, -3, -1]

from collections import deque
# N = int(input())
# P = list(map(int, input().split()))
Q = deque([(i, P[i-1]) for i in range(1, N+1)])
# print(Q)

while True:
    # print(Q)
    idx, x = Q.popleft()
    print(idx, end=" ")
    if not Q:
        break
    if x > 0:
        for i in range(x-1):
            Q.append(Q.popleft())
    else:
        for i in range(abs(x)):
            Q.appendleft(Q.pop())