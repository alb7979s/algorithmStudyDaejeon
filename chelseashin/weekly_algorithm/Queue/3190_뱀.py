import sys
sys.stdin = open("3190_input.txt")

from collections import deque

# 상 하 좌 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

chL = (2, 3, 1, 0)
chD = (3, 2, 0, 1)


N = int(input())    # 맵의 크기
B = [[0] * N for _ in range(N)]
for i in range(int(input())):    # 사과의 갯수만큼
    r, c = map(int, input().split())
    B[r-1][c-1] = 1

temp = dict()
for _ in range(int(input())):
    t, d = map(str, input().split())
    temp[int(t)] = d

snake = deque([(0, 0)])
B[0][0] = 2
dir = 3
time = 0
while True:
    r, c = snake[0]
    nr = r + dr[dir]
    nc = c + dc[dir]
    # 자기 자신 만나거나 벽 만나면 종료
    if (nr, nc) in snake or not (0 <= nr < N and 0 <= nc < N):
        print(time + 1)
        break
    # 빈 공간이면 나아가기
    if not B[nr][nc]:
        B[nr][nc] = 2
        snake.appendleft((nr, nc))
        tr, tc = snake.pop()    # 꼬리 제거
        B[tr][tc] = 0
    # 사과 있으면 나아가기
    if B[nr][nc] == 1:
        B[nr][nc] = 2
        snake.appendleft((nr, nc))

    time += 1
    if time in temp.keys():
        chdir = temp[time]
        if chdir == "L":
            dir = chL[dir]
        elif chdir == "D":
            dir = chD[dir]

    # for b in B:
    #     print(b)
    # print()