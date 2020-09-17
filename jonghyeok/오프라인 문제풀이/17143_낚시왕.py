from sys import*
from collections import*
input=stdin.readline
def move():
    global shark, a, tx, ty
    # print(shark)
    visit={}
    while shark:
        nx, ny, s, d, z = shark.popleft()
        if tx!=-1 and nx == tx and ny == ty: continue
        dx, dy = dd[d]
        a[nx, ny] = 0
        for _ in range(s):
            nx, ny = nx+dx, ny+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                d = chageD[d]
                dx, dy = dd[d]
                nx, ny = nx+2*dx, ny+2*dy
        # print(nx, ny)
        if (nx, ny) not in visit:
            visit[nx, ny] = [s, d, z]
        else:
            if visit[nx, ny][2] < z:
                visit[nx, ny] = [s, d, z]
    for k, v in visit.items():
        x, y = k
        s,d,z = v
        # print(k, v)
        a[x, y] = z
        shark.append((x,y,s,d,z))
    # print()
n, m, k = map(int,input().split())
shark=deque()
a={}
chageD=[1,0,3,2]
dd=[(-1,0),(1,0),(0,1),(0,-1)]
#0 초기화
for i in range(n):
    for j in range(m): a[i, j] = 0
for i in range(k):
    r, c, s, d, z = map(int,input().split())
    shark.append((r-1, c-1, s, d-1, z))
    a[r-1, c-1] = z
res=0
for i in range(m):
    tx, ty = -1, -1
    for j in range(n):
        if a[j, i]:
            res+=a[j, i]
            a[j, i]=0
            tx, ty = j, i
            break
    move()
print(res)
