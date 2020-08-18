import sys
sys.stdin = open('3055_input.txt')

from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def Gbfs():
    while GQ:
        r, c = GQ.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if raw[nr][nc] == 'X' or raw[nr][nc] == '*':
                continue
            if go[nr][nc] >= 0:
                continue
            if go[r][c] + 1 < water[nr][nc] or water[nr][nc] == -1:
                go[nr][nc] = go[r][c] + 1
                GQ.append((nr, nc))

def Wbfs():
    while WQ:
        r, c = WQ.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if raw[nr][nc] == 'D' or raw[nr][nc] == 'X':
                continue
            if water[nr][nc] >= 0:
                continue
            water[nr][nc] = water[r][c] + 1
            WQ.append((nr, nc))


R, C = map(int, input().split())
raw = [list(input()) for _ in range(R)]

go = [[-1] * C for _ in range(R)]
water = [[-1] * C for _ in range(R)]
# print(raw)
GQ = deque()
WQ = deque()
br, bc = 0, 0
for r in range(R):
    for c in range(C):
        if raw[r][c] == 'S':
            GQ.append((r, c))
            go[r][c] = 0
        if raw[r][c] == '*':
            WQ.append((r, c))
            water[r][c] = 0
        if raw[r][c] == 'D':
            br, bc = r, c

Wbfs()
# print('water', water)

# print('전', go)
Gbfs()
# print('후', go)

if go[br][bc] == -1:
    print("KAKTUS")
else:
    print(go[br][bc])