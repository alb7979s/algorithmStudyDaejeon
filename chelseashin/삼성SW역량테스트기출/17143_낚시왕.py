import sys
sys.stdin = open('17143_input.txt')

# 상 하 우 좌
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, 1, -1)

# 방향 바꾸기
rev = (0, 2, 1, 4, 3)

def move():
    check = [[0] * C for _ in range(R)]
    temp = []
    cnt = 0
    for nr in range(R):
        for nc in range(C):
            r, c = nr, nc
            if A[r][c]:
                cnt += 1
                speed, dir, size = A[r][c]
                A[r][c] = 0
                for _ in range(speed):  # 속도만큼
                    r += dr[dir]
                    c += dc[dir]
                    if not (0 <= r < R and 0 <= c < C):
                        dir = rev[dir]
                        if dir == 1:
                            r += dr[dir] - 1
                            c += dc[dir]
                        elif dir == 2:
                            r += dr[dir] + 1
                            c += dc[dir]
                        elif dir == 3:
                            r += dr[dir]
                            c += dc[dir] + 1
                        elif dir == 4:
                            r += dr[dir]
                            c += dc[dir] - 1
                if not check[r][c]:    # 없으면 새로 등록
                    temp.append((r, c))
                    check[r][c] = (speed, dir, size)
                else:   # 있으면 크기 비교
                    if check[r][c][2] < size:
                        check[r][c] = (speed, dir, size)
    for y, x in temp:
        A[y][x] = check[y][x]

# main
R, C, M = map(int, input().split())
if M == 0:
    print(0)
    exit()
A = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, speed, dir, size = map(int, input().split())
    A[r-1][c-1] = (speed, dir, size)

res = 0
for i in range(C):    # 매 열마다
    for j in range(R):
        if A[j][i]:
            res += A[j][i][2]
            A[j][i] = 0
            break
    move()
print(res)