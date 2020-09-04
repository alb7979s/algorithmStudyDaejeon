from sys import*
from collections import*
input=stdin.readline
def bfs(x, y):
    global a
    visit[x][y]=1
    q=deque([(x, y)])
    cnt=1
    sum=a[x][y]
    openList=[]
    openList.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny]: continue
            if L <= abs(a[nx][ny]-a[x][y]) <= R:
                q.append((nx, ny))
                sum+=a[nx][ny]
                cnt+=1
                visit[nx][ny]=1
                openList.append((nx, ny))
    if cnt==1: return 0
    else:
        for x, y in openList:
            a[x][y] = sum//cnt
        return 1
n, L, R = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
res = 0
while 1:
    f = True
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] and not visit[i][j]:
                if bfs(i, j):
                    f = False
    if f: break
    res+=1
print(res)
