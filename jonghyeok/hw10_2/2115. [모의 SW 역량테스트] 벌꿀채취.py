def solve(pos, arr, sum):
    res = 0
    if sum > c: return res
    if pos == m:
        ans=0
        for i in range(len(visit)):
            if visit[i]:
                ans += (arr[i]**2)
        return ans
    visit[pos]=1
    res = max(res, solve(pos+1, arr, sum+arr[pos]))
    visit[pos]=0
    res = max(res, solve(pos+1, arr, sum))
    return res
for tc in range(int(input())):
    n, m, c = map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    MAX = 0
    visit = [0]*m
    for ix in range(n):
        for iy in range(n-m+1):
            jx, jy = ix, iy+m
            while jx < n:
                while jy < n-m+1:
                    # print(a[ix][iy:iy+m]+a[jx][jy:jy+m])
                    MAX = max(MAX, solve(0, a[ix][iy:iy+m], 0)+solve(0, a[jx][jy:jy+m], 0))
                    jy += 1
                jy=0
                jx+=1
    print('#{} {}'.format(tc+1, MAX))
