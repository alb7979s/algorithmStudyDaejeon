from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def move(x, y, dx, dy):
    c=0
    while 1:
        c+=1
        x, y = x+dx, y+dy
        if a[x][y]=='#':
            return (x-dx, y-dy, c-1)
        if a[x][y]=='O':
            return (x, y, c)
def bfs(rx, ry, bx, by):
    q=deque()
    q.append((rx, ry, bx, by))
    visit[rx][ry][bx][by]=0
    while q:
        rx, ry, bx, by = q.popleft()
        if visit[rx][ry][bx][by]>10: break
        if a[rx][ry]=='O': return visit[rx][ry][bx][by]
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nrx, nry, nrc = move(rx, ry, dx, dy)
            nbx, nby, nbc = move(bx, by, dx, dy)
            if a[nbx][nby]=='O': continue
            if nrx==nbx and nry==nby:
                if nrc > nbc:
                    nrx, nry = nrx-dx, nry-dy
                else:
                    nbx, nby = nbx-dx, nby-dy
            if visit[nrx][nry][nbx][nby]!=-1: continue
            visit[nrx][nry][nbx][nby]=visit[rx][ry][bx][by]+1
            q.append((nrx, nry, nbx, nby))
    return -1
n, m = map(int,input().split())
a=[input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'B':
            bx, by = i, j
        elif a[i][j] == 'R':
            rx, ry = i, j
visit=[[[[-1]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]
print(bfs(rx, ry, bx, by))
