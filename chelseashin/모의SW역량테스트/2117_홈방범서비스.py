import sys
sys.stdin = open('2117_input.txt')

# k의 크기가 바뀜에 따라 계속 초기화하는 것이 아니라
# Q를 공유하면서 가장 겉부분 좌표를 담고 검사하고 담고 검사하는 방식으로 풀이

from collections import deque

# K에 따른 운영비용 리스트
KLst = [0] + [k * k + (k-1) * (k-1) for k in range(1, 25)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    global MAX
    home = 0
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    for size in range(1, 25):
        time = len(Q)
        for _ in range(time):
            r, c = Q.popleft()
            if city[r][c]:
                home += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                Q.append((nr, nc))
        # 보안회사의 이익이 0보다 크면
        if home * M - KLst[size] >= 0:
            MAX = max(MAX, home)
    return

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    MAX = float('-inf')

    # 중심 정하기
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print("#{} {}".format(tc+1, MAX))

    # 1 5
    # 2 4
    # 3 24
    # 4 48
    # 5 3
    # 6 65
    # 7 22
    # 8 22
    # 9 78
    # 10 400