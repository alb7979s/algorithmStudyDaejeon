import sys
sys.stdin = open('16234_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global flag
    Q = deque([(sr, sc)])
    visited[sr][sc] = 1
    temp = nation[sr][sc]
    nationList = [(sr, sc)]
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if L <= abs(nation[r][c] - nation[nr][nc]) <= R:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                temp += nation[nr][nc]
                nationList.append((nr, nc))

    n = len(nationList)
    if n == 1:
        return

    # 인구 이동
    flag = True
    avg = temp // n
    for r, c in nationList:
        nation[r][c] = avg
    return

# main
N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if nation[i][j] and not visited[i][j]:
                bfs(i, j)
    if flag:
        ans += 1
    else:
        break

print(ans)