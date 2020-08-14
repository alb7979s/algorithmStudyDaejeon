from sys import*
from itertools import*
input=stdin.readline
#회전
def rotate(b, r, c, s):
    for i in range(s+1):
        x, y = r-i, c-i
        temp = b[x][y]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            for j in range(i*2):
                nx, ny = x+dx, y+dy
                b[nx][ny], temp = temp, b[nx][ny]
                x, y = nx, ny
def solve(perm):
    res=INF
    #a배열 b배열에 복사
    b=[x[:] for x in a]
    for p in perm:
        x, y, c = info[p]
        x-=1; y-=1
        rotate(b, x, y, c)
    #모든 행마다 합의 최소값 구함
    for i in range(n):
        res = min(res, sum(b[i]))
    return res
n,m,k = map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
info=[list(map(int,input().split()))for _ in range(k)]
INF=1e9
res=INF
#순서 있이 모든 k 사용하는 순열
for perm in permutations(range(k), k):
    res = min(res, solve(perm))
print(res)
