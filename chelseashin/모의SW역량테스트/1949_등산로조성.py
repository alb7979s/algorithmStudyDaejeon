import sys
sys.stdin = open('1949_input.txt')

# swea 모의 테스트 문제

# 문제 정리
# 1. 등산로는 가장 높은 봉우리에서 시작
# 2. 등산로는 높은 지형에서 낮은 지형으로 가로 또는 세로 연결
# 2. 1. 높이가 같은 곳 대각선 연결 불가
# 3. 긴 등사로를 만들기 위해 딱 한 곳을 정해 최대 K 만큼 지형 깎기 가능.
# 4. 가장 긴 등산로 길이 출력

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 시작 좌표, 현재 거리, 기회
def dfs(r, c, dis, chance):
    global MAX
    if dis > MAX:
        MAX = dis
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if visited[nr][nc]:
            continue
        if M[nr][nc] < M[r][c]:
            visited[nr][nc] = 1
            dfs(nr, nc, dis+1, chance)
            visited[nr][nc] = 0
        else:
            if chance and M[r][c]+K > M[nr][nc] >= M[r][c]:
                chance = 0
                temp = M[nr][nc]
                M[nr][nc] = M[r][c] - 1     # 현 위치보다 1만 작도록 공사
                visited[nr][nc] = 1
                dfs(nr, nc, dis + 1, chance)
                visited[nr][nc] = 0
                M[nr][nc] = temp
                chance = 1

# main
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    MAX = float('-inf')
    top = 0
    for i in range(N):
        for j in range(N):
            if top < M[i][j]:
                top = M[i][j]

    for i in range(N):
        for j in range(N):
            if M[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1, 1)
                visited[i][j] = 0

    print("#{} {}".format(tc+1, MAX))

    # 1 6
    # 2 3
    # 3 7
    # 4 4
    # 5 2
    # 6 12
    # 7 6
    # 8 7
    # 9 10
    # 10 19