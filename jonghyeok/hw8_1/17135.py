#priority queue 사용
from sys import*
from heapq import*
input=stdin.readline
def cal():
    b = [x[:] for x in a]
    died = 0
    dieCheck=[[0]*m for _ in range(n)]
    for sx in range(n-1, -1, -1):
        archerX = sx+1
        for archerY in archers:
            pq = []
            visit=[[0]*m for _ in range(n)]
            heappush(pq, (0, archerY, archerX))
            searched=False
            while 1:
                if not pq: break
                lenpq = len(pq)
                for i in range(lenpq):
                    c, y, x = heappop(pq)
                    for dx, dy in [(0, 1), (-1, 0), (0, -1)]:    #아래는 갈 필요 없음
                        nx, ny = x+dx, y+dy
                        if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or c+1 > d: continue
                        if b[nx][ny]:searched=True
                        visit[nx][ny]=1
                        heappush(pq,(c+1, ny, nx))
                if searched:
                    while pq:
                        c, y, x = heappop(pq)
                        if b[x][y]:
                            dieCheck[x][y]=1
                            break
                    break
        for i in range(n):
            for j in range(m):
                if dieCheck[i][j]:
                    dieCheck[i][j]=0
                    b[i][j]=0
                    died+=1
        for j in range(m):
            b[sx][j]=0
    return died
def solve(pos, cnt):
    global archers
    res=0
    if cnt > 3: return 0
    if pos == m:
        if cnt == 3:
            res = max(res, cal())
        return res
    archers.append(pos)
    res = max(res, solve(pos+1, cnt+1))
    archers.pop()
    res = max(res, solve(pos+1, cnt))
    return res
n,m,d=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
archers = []
print(solve(0, 0))
