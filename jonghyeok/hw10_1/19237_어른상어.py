from sys import*
from collections import*
input=stdin.readline
def solve():
    q=deque()
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                #처음 타이머 k로 했다가 틀렸었음, 항상 제출 전에 예제랑 비교하면서 디테일하게 살펴보기
                visit[i][j] = [k-1, a[i][j]]                      #생존타이머, 상어번호
                q.append((i, j, a[i][j], defaultD[a[i][j]-1]-1))  #x, y, 상어, 방향
    for t in range(1001):   #1001동안~
        # for i in range(n):
        #     for j in range(n):
        #         print(visit[i][j],end=' ')
        #     print()
        # print(t)
        lq = len(q)
        if lq == 1: return t
        dic = {}
        for i in range(lq):
            x, y, s, d = q.popleft()
            isMove = False
            for j in range(4):
                nd = pd[s-1][d][j]
                dx, dy = dd[nd]
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny]: continue
                isMove = True
                if (nx, ny) not in dic:
                    dic[nx, ny] = [s, nd]
                else:
                    if dic[nx, ny][0] > s:
                        dic[nx, ny] = [s, nd]
                break
            if not isMove:
                for j in range(4):
                    nd = pd[s-1][d][j]
                    dx, dy = dd[nd]
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>n-1:continue
                    if visit[nx][ny][1] == s:
                        dic[nx, ny] = [s, nd]
                        break
        for i in range(n):
            for j in range(n):
                if visit[i][j] and visit[i][j][0] <= t:
                    visit[i][j]=0
        for (x, y), (s, d) in dic.items():
            visit[x][y] = [k+t, s]
            q.append((x, y, s, d))
    return -1
dd=[(-1,0),(1,0),(0,-1),(0,1)]  #UDLR
n, m, k = map(int,input().split())
pd = [[]for _ in range(m)]
a=[list(map(int,input().split()))for _ in range(n)]
defaultD = list(map(int,input().split()))
for i in range(m):
    for j in range(4):
        temp=list(map(int,input().split()))
        pd[i].append([x-1 for x in temp])
print(solve())
