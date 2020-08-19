import sys
sys.stdin = open('17471_input.txt')

from collections import deque

def bfs():
    # devided에서 1인 것 나누어지는지 조사
    Q = deque()
    visited = [0] * N
    for i in range(N):
        if divided[i] == 1:
            Q.append(i)
            visited[i] = 1
            break
    while Q:
        start = Q.popleft()
        for end in range(N):
            if visited[end] == 1:
                continue
            if divided[end] == 0:
                continue
            if G[start][end]:
                visited[end] = 1
                Q.append(end)
    if visited != divided:
        return False
    Q.clear()
    visited = [1] * N

    # devided에서 0인 것 나누어지는지 조사
    for i in range(N):
        if divided[i] == 0:
            Q.append(i)
            visited[i] = 0
            break

    while Q:
        s = Q.popleft()
        for end in range(N):
            if visited[end] == 0:
                continue
            if divided[end] == 1:
                continue
            if G[s][end]:
                visited[end] = 0
                Q.append(end)
    if divided != visited:
        return False
    return True

# 0과 1로 구역 나누기
def dfs(depth):
    global MIN
    if depth == N:
        if sum(divided) == 0 or sum(divided) == N:
            return
        print(divided)
        if bfs():       # 구역 나누기 가능하면
            A = 0
            for i in range(N):
                if divided[i]:   # 1일 때
                    A += population[i]
            B = sum(population) - A
            if MIN > abs(A-B):
                MIN = abs(A-B)
        return
    for i in [0, 1]:
        divided.append(i)
        dfs(depth + 1)
        divided.pop()

# main
N = int(input())
population = list(map(int, input().split()))
MIN = float('inf')

# 인접행렬 리스트
G = [[0] * (N) for _ in range(N)]
for i in range(N):
    for j in list(map(int, input().split()))[1:]:
        G[i][j-1] = 1

divided = []
dfs(0)
if MIN == float('inf'):
    print(-1)
else:
    print(MIN)