# Brute Force / Simulation 문제

import sys
sys.stdin = open('12100_input.txt')
input = sys.stdin.readline
from collections import deque

# main
N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
ans = 0
Q = deque()

def get(i, j):
    if B[i][j]:
        Q.append(B[i][j])
        B[i][j] = 0     # Q에 넣은 블록은 0으로 바꿔주기

# 시작 좌표, 합치는 방향
def merge(r, c, dr, dc):
    while Q:
        x = Q.popleft()
        if not B[r][c]:         # 빈 칸이면
            B[r][c] = x         # 그대로 놓기
        elif B[r][c] == x:      # 값 일치하면
            B[r][c] *= 2        # 합쳐지므로 2배
            r += dr
            c += dc
        else:                   # 값 다르면
            r += dr
            c += dc
            B[r][c] = x         # 한칸 뒤에 블록 놓기

def move(dir):
    # 위로 이동
    if dir == 0:
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)   # row 인덱스 1씩 증가하면서 아래쪽 블락들을 합침
    # 아래로 이동
    elif dir == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1, j, -1, 0)    # row 인덱스 1씩 감소하면서 위쪽 블록들을 합침
    # 오른쪽으로 이동
    elif dir == 2:
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)     # column 인덱스 증가 오른쪽으로 이동하며 블록 합침
    # 왼쪽으로 이동
    elif dir == 3:
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i, j)
            merge(i, N-1, 0, -1)    # column 인덱스 감소 왼쪽으로 이동하며 블록 합침

def dfs(depth):
    global ans, B
    if depth == 5:
        for i in range(N):
            ans = max(ans, max(B[i]))   # 맵에서 가장 큰 값 리턴
        return
    b = [x[:] for x in B]   # 방향 바꾸기 전 원래의 보드 상태 기억
    for d in range(4):
        move(d)         # 방향으로 이동
        dfs(depth+1)    # 재귀호출
        B = [x[:] for x in b]   # 되돌리기

dfs(0)
print(ans)