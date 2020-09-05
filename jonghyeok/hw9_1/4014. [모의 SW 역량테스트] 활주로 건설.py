# import sys
# sys.stdin = open('C:/projects/mysite/algorithms/test.txt')

def solve(x, y, dx, dy):
    cnt=1
    for i in range(n-1):
        nx, ny = x+dx, y+dy
        diff = a[nx][ny] - a[x][y]
        if diff == 0:cnt += 1
        elif abs(diff) > 1: return 0
        else:
            if diff==1: #뒤가 클 때
                if cnt < L: return 0
                cnt=1
            else:
                if cnt < 0: return 0
                cnt = -L+1
        x, y = nx, ny
    if cnt<0: return 0
    else: return 1
for tc in range(int(input())):
    n, L = map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n)]
    res=0
    for i in range(n):
        res += solve(i, 0, 0, 1)
        res += solve(0, i, 1, 0)
    print('#{} {}'.format(tc+1, res))
