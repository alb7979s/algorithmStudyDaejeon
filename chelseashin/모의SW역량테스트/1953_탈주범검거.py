import sys
sys.stdin = open('1953_input.txt')

from collections import deque

# 상 하 좌 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 7가지 종류 지하 터널에서 나갈 수 있는 방향
direction = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

def change(n):
    if n == 0: return 1
    elif n == 1: return 0
    elif n == 2: return 3
    elif n == 3: return 2

def bfs(sr, sc):
    cnt = 1
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        if visited[r][c] == L:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc] or not A[nr][nc]:
                continue
            if direction[A[r][c]-1][i] and direction[A[nr][nc]-1][change(i)]:
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1
                Q.append((nr, nc))
    return cnt

# main
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    print("#{} {}".format(tc+1, bfs(R, C)))

    # 1 5
    # 2 15
    # 3 29
    # 4 67
    # 5 71