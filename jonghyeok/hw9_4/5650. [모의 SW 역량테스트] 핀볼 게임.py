# import sys
# sys.stdin = open('test.txt')
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
blocks = [[],
          [2, 0, 3, 1],
          [2, 3, 1, 0],
          [1, 3, 0, 2],
          [3, 2, 0, 1],
          [2, 3, 0, 1]]
def play(x, y, d):
    nx, ny = x, y
    cnt=0
    while 1:
        dx, dy = dd[d]
        nx, ny = nx+dx, ny+dy
        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 or a[nx][ny]==5:
            nx, ny, d = nx-dx, ny-dy, blocks[5][d]
            cnt+=1
        if 1<= a[nx][ny] <= 4:
            d = blocks[a[nx][ny]][d]
            cnt+=1
        elif a[nx][ny]==-1 or (x==nx and y==ny): return cnt
        elif 6<=a[nx][ny]<=10:
            nx, ny = change[nx, ny]
for tc in range(int(input())):
    n=int(input())
    a=[list(map(int,input().split()))for _ in range(n)]
    change = {}
    warm = {}
    for i in range(n):
        for j in range(n):
            if 6<= a[i][j] <= 10:
                if a[i][j] not in warm:
                    warm[a[i][j]] = (i, j)
                else:
                    x, y = warm[a[i][j]]
                    change[i, j] = (x, y)
                    change[x, y] = (i, j)
    res = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                for k in range(4):
                    res = max(res, play(i, j, k))
    print('#{} {}'.format(tc+1, res))
