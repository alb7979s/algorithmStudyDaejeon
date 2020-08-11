#3055
from sys import*
from collections import*
def input():
    return stdin.readline().strip()
INF=987654321
n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(input())
water=[]
ex,ey=0,0
for i in range(n):
    for j in range(m):
        if arr[i][j]=='S':
            start=[i,j]
        elif arr[i][j]=='D':
            ex,ey = i, j
        elif arr[i][j]=='*':
            water.append([i,j])

dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
w_visit=[[INF]*m for i in range(n)]
for i,j in water:
    q.append([i,j])
    w_visit[i][j]=0

while q:
    x,y=q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ( nx < 0 or ny < 0 or nx > n-1 or ny > m-1 or
             arr[nx][ny]!='.' or w_visit[nx][ny]!=INF ): continue
        w_visit[nx][ny]=w_visit[x][y]+1
        q.append([nx,ny])
q=deque()
visit=[[-1]*m for i in range(n)]
q.append(start)
t1,t2=start
visit[t1][t2]=0
while q:
    x,y=q.popleft()
    if x == ex and y == ey:
        print(visit[x][y])
        exit()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (nx<0 or ny<0 or nx>n-1 or ny>m-1 or (arr[nx][ny]!='.' and arr[nx][ny]!='D')
            or visit[nx][ny]!=-1 or visit[x][y]+1 >= w_visit[nx][ny]):
            continue
        visit[nx][ny]=visit[x][y]+1
        q.append([nx,ny])
print('KAKTUS')
        
