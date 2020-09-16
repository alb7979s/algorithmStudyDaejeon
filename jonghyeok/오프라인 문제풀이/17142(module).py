from sys import*
from collections import*
from itertools import*
input=stdin.readline
def bfs(activeList):
    visit=[[-1]*n for _ in range(n)]
    q=deque()
    cnt=0
    for x, y in activeList:
        q.append((x, y))
        visit[x][y]=0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1), (0,-1), (1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]==1 or visit[nx][ny]!=-1: continue
            if not a[nx][ny]:
                cnt += 1
            visit[nx][ny]=visit[x][y]+1
            q.append((nx, ny))
            if cnt==zeroCnt:
                return visit[nx][ny]
    return float('INF')
n,m=map(int,input().split())
a=[]
virusList=[]
virusCnt=0
activeList=[]
zeroCnt=0
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(n):
        if not a[i][j]:
            zeroCnt += 1
        elif a[i][j]==2:
            virusList.append((i, j))
            virusCnt += 1
res = float('INF')
if not zeroCnt: print(0)
else:
    for c in combinations(virusList, m):
        res = min(res, bfs(c))
    print(res if res != float('INF') else -1)
