# 가장 일반화된 풀이

import sys
sys.stdin = open('13460_input.txt')
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def move(r, c, dr, dc):
    cnt = 0     # 이동 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while B[r+dr][c+dc] != "#" and B[r][c] != "O":
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

def bfs(rr, rc, br, bc):
    check = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    check[rr][rc][br][bc] = 1
    Q = deque([(rr, rc, br, bc, 1)])    # 위치 정보와 depth(몇번 구슬 움직였는지)
    while Q:
        rr, rc, br, bc, depth = Q.popleft()     # FIFO(최단거리)
        if depth > 10:  # 종료조건
            break
        # 4방향 기울이기
        for i in range(4):
            nrr, nrc, rcnt = move(rr, rc, dr[i], dc[i])
            nbr, nbc, bcnt = move(br, bc, dr[i], dc[i])
            # 파란 구슬이 구멍에 떨어지면 다른 방향 탐색
            if B[nbr][nbc] == "O":
                continue
            # 빨간 구슬이 구멍에 떨어진다면(성공)
            if B[nrr][nrc] == "O":
                print(depth)
                return
            # 빨간 구슬과 파란 구슬이 동시에 같은 칸이면
            if nrr == nbr and nrc == nbc:
                if rcnt > bcnt:     # 이동거리 많은 구슬을 한 칸 뒤로
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]
            # BFS 탐색 마치고, 방문 여부 확인
            if not check[nrr][nrc][nbr][nbc]:
                check[nrr][nrc][nbr][nbc] = 1
                Q.append((nrr, nrc, nbr, nbc, depth+1))
    # 실패
    print(-1)
    return

# main
N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]

rr, rc, br, bc = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if B[i][j] == "R":
            rr, rc = i, j
        elif B[i][j] == "B":
            br, bc = i, j

bfs(rr, rc, br, bc)