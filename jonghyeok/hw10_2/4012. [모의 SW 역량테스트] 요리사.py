INF=1e9
def cal():
    t1, t2 = 0, 0
    for i in range(n):
        for j in range(i+1):
            if i==j: continue
            if visit[i] and visit[j]:
                t1 += a[i][j] + a[j][i]
            if not visit[i] and not visit[j]:
                t2 += a[i][j] + a[j][i]
    return abs(t1-t2)
def solve(pos, cnt):
    res=INF
    if cnt > n//2: return res
    if pos == n:
        if cnt == n//2:
            res = min(res, cal())
        return res
    visit[pos]=1
    res = min(res, solve(pos+1, cnt+1))
    visit[pos]=0
    res = min(res, solve(pos+1, cnt))
    return res
for tc in range(int(input())):
    n = int(input())
    visit=[0]*n
    a=[list(map(int,input().split()))for _ in range(n)]
    print('#{} {}'.format(tc+1, solve(0, 0)))
