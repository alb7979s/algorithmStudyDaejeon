import sys
sys.stdin = open('17142_input.txt')

from itertools import combinations
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(A):
    global Q, space, min_time
    cnt = 0
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if lab[nr][nc] == 1 or A[nr][nc]:   # 벽이거나 이미 간 곳이면
                continue
            if not lab[nr][nc]:     # 공간일 때만 + 1 해주기
                cnt += 1
            A[nr][nc] = A[r][c] + 1
            Q.append((nr, nc))
        if space == cnt:
            return A[r][c]
    return float('inf')

# main
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
min_time = float('inf')

space = 0   # 빈 공간 갯수
virus = []  # 바이러스 위치 좌표 리스트
for i in range(N):
    for j in range(N):
        if lab[i][j] == 0:
            space += 1
        if lab[i][j] == 2:
            virus.append((i, j))
# 아예 빈 공간이 없으면
if space == 0:
    print(0)
else:
    for comb in combinations(range(len(virus)), M):
        new = [[0] * N for _ in range(N)]
        Q = deque()
        for c in comb:
            i, j = virus[c]
            new[i][j] = 1
            Q.append((i, j))
        min_time = min(min_time, bfs(new))
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)