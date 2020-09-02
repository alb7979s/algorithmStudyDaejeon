#import sys
# sys.stdin = open('C:/projects/mysite/algorithms/test.txt')
from collections import*
#BFS모양으로 퍼짐
#운영비용 = k**2+(k-1)**2
#손해 보지 않게 가장 많이 서비스 제공하는 집의 수

#최적화(일단 풀고 생각)
#k크기에 따른 비용 구해놓을 수 있을듯
cost = [0]*22
for i in range(1, 22):
    cost[i] = i**2 + (i-1)**2
def bfs(x, y):
    global res
    q=deque()
    visit=[[0]*n for _ in range(n)]
    q.append((x, y))
    visit[x][y]=1
    cnt=1 if a[x][y] else 0
    for i in range(1, n+2):
        if cnt*m >= cost[i]: res = max(res, cnt)
        lq = len(q)
        for j in range(lq):
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1 ,0)]:
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny]:continue
                q.append((nx, ny))
                visit[nx][ny]=1
                if a[nx][ny]: cnt+=1

for tc in range(int(input())):
    n, m = map(int,input().split())     #N*N도시, m은 하나의 집당 지출 가능한 비용
    a=[list(map(int,input().split()))for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            bfs(i, j)
    print('#%d %d'%(tc+1, res))
