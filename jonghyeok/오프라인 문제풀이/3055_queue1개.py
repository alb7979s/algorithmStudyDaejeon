from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def bfs():
    while q:
        x, y, f = q.popleft()
        if a[x][y] == 'D' and f: return visit[x][y]
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny]!=-1 or a[nx][ny]=='X': continue
            if a[nx][ny]=='D' and not f: continue
            q.append((nx, ny, f))
            visit[nx][ny] = visit[x][y]+1
    return -1
n,m=map(int,input().split())
a=[]
q=deque()
for i in range(n):
    a.append(input())
    for j in range(m):
        if a[i][j] == 'S':
            sx, sy = i, j
        elif a[i][j] == '*':    #물 0
            q.append((i, j, 0))
q.append((sx, sy, 1))   #도치 1
visit = [[-1] * m for _ in range(n)]
for x, y, f in q:
    visit[x][y]=0
res = bfs()
print(res if res!=-1 else 'KAKTUS')
