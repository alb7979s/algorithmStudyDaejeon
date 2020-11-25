from sys import*
input=stdin.readline
INF = int(1e9)
ans = [-1]*16
res = INF
def solve(pos, p, f, s, v, c):
    global res
    if pos == n:
        if p>=mp and f>=mf and s>=ms and v>=mv:
            if res > c:
                res = c
                # print(res, picked)
                for i in range(16):
                    if i < len(picked):
                        ans[i] = picked[i]+1
                    else:
                        ans[i] = -1
        return res
    picked.append(pos)
    res = min(res, solve(pos+1, p+info[pos][0], f+info[pos][1], s+info[pos][2], v+info[pos][3], c+info[pos][4]))
    picked.pop()
    res = min(res, solve(pos+1, p, f, s, v, c))
    return res
n=int(input())
picked=[]
mp, mf, ms, mv = map(int,input().split())
info = []

for i in range(n):
    info.append(list(map(int,input().split())))

res = solve(0, 0, 0, 0, 0, 0)
if res == INF: print(-1)
else:
    print(res)
    for x in ans:
        if x==-1: break
        print(x, end=' ')
