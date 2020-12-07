import sys
sys.stdin = open("1021_input.txt")

from collections import deque

N, M = map(int, input().split())
Q = deque([i for i in range(1, N+1)])

# 뽑아야 하는 숫자 리스트
pick = list(map(int, input().split()))

cnt = 0
for i in range(M):
    leftPos = Q.index(pick[i])  # 왼쪽부터의 위치
    rightPos = len(Q) - leftPos # 오른쪽부터의 위치
    # 뽑아야 하는 위치가 앞쪽에 더 가깝다면 왼쪽으로 이동
    if leftPos < rightPos:
        for _ in range(leftPos):
            Q.append(Q.popleft())
            cnt += 1
    # 뽑아야 하는 위치가 뒷쪽에 더 가깝다면 오른쪽으로 이동
    else:
        for _ in range(rightPos):
            Q.appendleft(Q.pop())
            cnt += 1
    Q.popleft()

print(cnt)