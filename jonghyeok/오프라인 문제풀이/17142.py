from sys import*
from collections import*
input=stdin.readline
setrecursionlimit(10**6)
def bfs():
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
def solve(pos, cnt):
    global activeList
    res=float('INF')
    if cnt>m: return res
    if pos == virusCnt:
        if cnt == m:
            res=min(res, bfs())
        return res
    x, y = virusList[pos]
    activeList.append((x, y))
    res = min(res, solve(pos+1, cnt+1))
    activeList.pop()
    res = min(res, solve(pos+1, cnt))
    return res
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
if not zeroCnt: print(0)
else:
    res = solve(0, 0)
    print(res if res!=float('INF') else -1)
