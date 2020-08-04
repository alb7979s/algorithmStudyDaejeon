#시간초과
from sys import*
input=stdin.readline
setrecursionlimit(10**6)
def searchD(dx, dy):
    if dx==0 and dy==1: return 0
    if dx==1 and dy==0: return 1
    if dx==1 and dy==1: return 2
def solve(x, y, d):
    global res
    if x==n-1 and y==n-1:
        res += 1
        return
    for dx, dy in dd[d]:
        nx, ny, nd = x+dx, y+dy, searchD(dx, dy)
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]: continue
        if nd == 2 and (a[nx][ny-1] or a[nx-1][ny]): continue
        solve(nx, ny, nd)
    return
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
dd=[[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 1), (1, 0)]]
res=0
solve(0, 1, 0)
print(res)
