from sys import*
input=stdin.readline
weight = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05]
loc = [[(-1, 1), (1, 1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, -1), (1, -1), (0, -2)], #L
       [(-1, -1), (-1, 1), (0, -1), (0, 1),(0,-2), (0, 2), (1, -1), (1, 1), (2, 0)],    #D
       [(-1, -1),(1,-1),(-1,0), (1,0), (-2,0), (2,0), (-1, 1), (1, 1), (0, 2)],         #R
       [(1, -1), (1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (-1, -1), (-1, 1), (-2, 0)]] #U

def spread(x, y, d, sand):
    global board, res
    #첨엔 d 나눠서 생각할라 했는데 어느 방향이든 상대적인 위치 같네유?
    staticSand = sand
    for i in range(9):
        dx, dy = loc[d][i]
        value =  int(staticSand * weight[i])
        sand -= value
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1:
            res += value
            continue
        board[nx][ny] += value
    return sand
n=int(input())
board=[list(map(int,input().split()))for _ in range(n)]
dd = [(0,-1),(1,0),(0,1),(-1,0)]    #LDRU
x, y = n//2, n//2
s=1
d=-1
res = 0
for i in range(1, n):
    for j in range(2):
        d = (d + 1) % 4
        dx, dy = dd[d]
        for k in range(i):
            x, y = x+dx, y+dy
            nx, ny = x+dx, y+dy
            if nx < 0 or ny<0 or nx>n-1 or ny>n-1:
                res += spread(x, y, d, board[x][y])
            else:
                board[nx][ny] += spread(x, y, d, board[x][y])
            # board[x][y] += board[x - dx][y - dy]
#맨윗줄 처리
d = (d+1)%4
dx, dy = dd[d]
for i in range(n-1):
    x, y = x + dx, y + dy
    nx, ny = x + dx, y + dy
    if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
        res += spread(x, y, d, board[x][y])
    else:
        board[nx][ny] += spread(x, y, d, board[x][y])
    # board[x][y] += board[x - dx][y - dy]
print(res)
