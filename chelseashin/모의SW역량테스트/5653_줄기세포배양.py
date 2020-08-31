import sys
sys.stdin = open('5653_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    hour = 0
    while Q and hour < K:
        rotation = len(Q)
        for _ in range(rotation):
            r, c = Q.popleft()
            origin = raw_data[r][c][0]
            life = raw_data[r][c][1]
            if life == 0:
                continue
            if origin != life:
                raw_data[r][c][1] -= 1
                Q.append((r, c))    # 한번 더 검사해줘야하기 때문에
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N+K and 0 <= nc < M+K):
                    continue
                if raw_data[nr][nc] == 0:
                    raw_data[nr][nc] = [origin, 2 * origin, hour]
                    Q.append((nr, nc))
                elif origin > raw_data[nr][nc][0] and hour == raw_data[nr][nc][2]:
                    raw_data[nr][nc] = [origin, 2*origin, hour]
            # 활성화 되기까지의 시간
            raw_data[r][c][1] -= 1
            Q.append((r, c))
        hour += 1
# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    raw_data = [[0] * (K+M) for _ in range(K+N)]
    for r in range(N):
        raw_data[r + (K//2)][K//2:(K//2)+M] = list(map(int, input().split()))
    # print(raw_data)
    result = 0
    Q = deque()
    for r in range(N+K):
        for c in range(M+K):
            if raw_data[r][c]:
                raw_data[r][c] = [raw_data[r][c], 2*raw_data[r][c], 0]
                Q.append((r, c))
    # print(raw_data)
    bfs()
    for r in range(N+K):
        for c in range(M+K):
            if raw_data[r][c] == 0:
                continue
            elif raw_data[r][c][1] != 0:
                result += 1
    print("#{} {}".format(tc+1, result))