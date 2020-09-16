import sys
sys.stdin = open('5644_input.txt')

from collections import deque

# 상 우 하 좌
dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)

# BC 설치, 범위와 성능 표시
def install(idx, sr, sc, coverage, performance):
    raw[idx][sr][sc] = performance
    visited = [[-1] * 10 for _ in range(10)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        if visited[r][c] == coverage:
            break
        for i in range(1, 5):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < 10 and 0 <= nc < 10):
                continue
            if visited[nr][nc] >= 0:
                continue
            visited[nr][nc] = visited[r][c] + 1
            raw[idx][nr][nc] = performance
            Q.append((nr, nc))

def dfs(depth, total, user):
    global N, each
    temp = 0
    if depth == 2:
        return total
    r, c = user[depth][0], user[depth][1]
    for i in range(N):
        if selected[i]:
            continue
        if not raw[i][r][c]:
            continue
        selected[i] = 1
        temp = max(temp, dfs(depth+1, total + raw[i][r][c], user))
        selected[i] = 0
    temp = max(temp, dfs(depth+1, total, user))
    return temp

# main
T = int(input())
for tc in range(T):
    M, N = map(int, input().split())    # 이동정보 수, 설치된 BC 수
    info = [list(map(int, input().split())) for _ in range(2)]
    raw = [[[0] * 10 for _ in range(10)] for _ in range(N)]

    # BC 정보 저장
    for i in range(N):
        x, y, C, P = map(int, input().split())
        install(i, y-1, x-1, C, P)

    selected = [0] * N
    user = [[0, 0], [9, 9]]
    MAX = dfs(0, 0, user)   # 시작좌표
    # 1분마다
    for i in range(M):
        # 사용자 A, B 동시에 이동 처리
        for j in range(2):
            user[j][0] += dr[info[j][i]]
            user[j][1] += dc[info[j][i]]
        MAX += dfs(0, 0, user)

    print("#{} {}".format(tc+1, MAX))

    #1 1200
    #2 3290
    #3 16620
    #4 40650
    #5 52710