from sys import*
from collections import*
input=stdin.readline
#UnionFind
def find(u):
    if parent[u] == u: return u
    parent[u] = find(parent[u])
    return parent[u]
def union(u, v):
    u = find(u)
    v = find(v)
    if u==v: return False
    parent[u] = v
    return True
#섬들 번호 붙여줌
def bfs(x, y, idx):
    q=deque()
    q.append((x,y))
    indexing[x][y]=idx
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or indexing[nx][ny]\
               or not a[nx][ny]:continue
            indexing[nx][ny]=idx
            q.append((nx,ny))
n,m=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
indexing = [[0]*m for _ in range(n)]
idx=1
for i in range(n):
    for j in range(m):
        if a[i][j] and not indexing[i][j]:
            bfs(i, j, idx)
            idx+=1
info=[]
#행
for i in range(n):
    prevY = -1
    cnt = 0
    for j in range(m):
        if a[i][j]:
            if cnt >= 2 and prevY!=-1 and indexing[i][prevY] != indexing[i][j]:
                info.append((cnt, i, prevY, i, j))
            cnt=0
            prevY=j
        else:
            cnt+=1
#열
for i in range(m):
    prevX = -1
    cnt = 0
    for j in range(n):
        if a[j][i]:
            if cnt >= 2 and prevX!=-1 and indexing[prevX][i] != indexing[j][i]:
                info.append((cnt, prevX, i, j, i))
            cnt=0
            prevX=j
        else:
            cnt+=1
parent=[i for i in range(idx)]
info.sort()
res=0
c=1
#MST
for i in info:
    cnt, x1, y1, x2, y2 = i
    u = indexing[x1][y1]
    v = indexing[x2][y2]
    if union(u, v):
        c+=1
        res+=cnt
    if c == idx-1:
        print(res)
        exit()
print(-1)
