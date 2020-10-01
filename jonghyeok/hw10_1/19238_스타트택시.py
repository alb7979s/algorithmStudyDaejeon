from sys import*
from collections import*
from heapq import*
input=stdin.readline
def solve():
    global k
    q=deque()
    q.append((0, sx-1, sy-1))
    cnt = 0
    status = 0      #0 시작 찾음, 1 도착점 찾음, 2도착점 찾은 상태
    ex, ey = -1, -1
    while 1:
        if cnt == m: return k
        if not q: break
        visit = [[0]*n for _ in range(n)]
        while 1:
            lq = len(q)
            if not q: break
            pq = []
            for i in range(lq):
                c, x, y = q.popleft()
                if c > k: return -1
                if status==0 and a[x][y]:
                    heappush(pq, (c, x, y))
                    continue
                if status and x==ex and y==ey:
                    cnt+=1
                    k += c
                    status = 2
                    q=deque()
                    q.append((0, x, y))
                    break
                for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or a[nx][ny]==1: continue
                    visit[nx][ny]=1
                    q.append((c+1, nx, ny))
            if status==0 and pq:
                c, x, y = heappop(pq)
                ex, ey = a[x][y]
                a[x][y]=0
                q=deque()
                k -= c
                q.append((0, x, y))
                status=1
                break
            if status==2:
                status=0
                break
    return -1

n, m, k= map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
sx, sy = map(int,input().split())
for i in range(m):
    x, y, ex, ey = map(int,input().split())
    a[x-1][y-1] = [ex-1, ey-1]
print(solve())
