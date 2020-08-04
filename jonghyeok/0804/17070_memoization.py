from sys import*
input=stdin.readline
def searchD(dx, dy):
    if dx==0 and dy==1: return 0
    if dx==1 and dy==0: return 1
    if dx==1 and dy==1: return 2
def solve(x, y, d):
    if x==n-1 and y==n-1: return 1
    if mem[x][y][d]!=-1: return mem[x][y][d]
    mem[x][y][d]=0
    for dx, dy in dd[d]:
        nx, ny, nd = x+dx, y+dy, searchD(dx, dy)
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]: continue
        if nd == 2 and (a[nx][ny-1] or a[nx-1][ny]): continue
        mem[x][y][d] += solve(nx, ny, nd)
    return mem[x][y][d]
n=int(input())
mem = [[[-1]*3 for _ in range(n)] for _ in range(n)]
a=[list(map(int,input().split()))for _ in range(n)]
dd=[[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 1), (1, 0)]]
print(solve(0, 1, 0))

