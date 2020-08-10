from sys import*
setrecursionlimit(10**6)
input=stdin.readline
def check(x, y, pos):
    if paperCnt[pos] <= 0: return False
    for i in range(x, x+pos+1):     #색종이 크기만큼
        for j in range(y, y+pos+1):
            if i>9 or j>9 or not a[i][j]: return False
    #위에서 안걸렸으면 확인 완료, 색칠
    for i in range(x, x+pos+1):
        for j in range(y, y+pos+1):
            a[i][j] = 0
    return 1
def solve(pos, cnt, totalCnt):
    global a, res
    if totalCnt == drawCnt: return cnt
    if pos == drawCnt or res <= cnt: return res
    x, y = drawList[pos]
    if a[x][y]:
        for i in range(5):
            if check(x, y, i):
                paperCnt[i] -= 1
                res = min(res, solve(pos+1, cnt+1, totalCnt+(i+1)**2))
                paperCnt[i] += 1
                for u in range(x, x+i+1):
                    for v in range(y, y+i+1):
                        a[u][v] = 1
    else:
        res = min(res, solve(pos+1, cnt, totalCnt))
    return res
a=[]
drawCnt = 0
drawList = []
paperCnt=[5]*5
INF=1e9
res = INF
for i in range(10):
    a.append(list(map(int,input().split())))
    for j in range(10):
        if a[i][j]:
            drawCnt += 1
            drawList.append((i, j))
ans=solve(0, 0, 0)
print(ans if ans!=INF else -1)
