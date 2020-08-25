#각 코어마다 4방향 완탐, 테두리는 살필 필요 없음
def connect(x, y, dx, dy):
    c=0
    while 1:
        c+=1
        x, y = x+dx, y+dy
        if a[x][y]: return 0
        if x==0 or y==0 or x==n-1 or y==n-1: return c
        a[x][y]=1
def solve(pos, cnt, res):
    global maxCnt, minRes, a
    if pos == len(coreList):
        if cnt >= maxCnt:
            if cnt > maxCnt:
                minRes = res
            else:
                minRes = min(minRes, res)
            maxCnt=cnt
        return minRes
    x, y = coreList[pos]
    b=[x[:]for x in a]
    for dx, dy in [(0, 1),(0, -1),(-1, 0),(1, 0)]:
        temp = connect(x, y, dx, dy)
        if temp:
            solve(pos+1, cnt+1, res+temp)
        a = [x[:] for x in b]
    solve(pos+1, cnt, res)
    return minRes
INF=int(1e9)
for tc in range(int(input())):
    n=int(input())
    a=[list(map(int,input().split()))for _ in range(n)]
    coreList = []
    maxCnt, minRes = 0, INF
    for i in range(1, n-1):
        for j in range(1, n-1): #테두린 필요 없음
            if a[i][j]:
                coreList.append((i, j))
    print("#{} {}".format(tc+1, solve(0, 0, 0)))
