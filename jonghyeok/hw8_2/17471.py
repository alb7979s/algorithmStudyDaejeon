from sys import*
from collections import*
setrecursionlimit(10**6)
input=stdin.readline
def bfs(picked):
    redSum, blueSum, red, blue = 0, 0, 0, 0
    rq, bq = deque(), deque()
    for i in range(n):
        if picked & (1<<i): #선택 되었으면 레드
            if not rq: rq.append(i)
            redSum += popul[i]
            red |= (1<<i)
        else:
            if not bq: bq.append(i)
            blueSum += popul[i]
            blue |= (1<<i)
    #아예 선택 안된거 있으면 INF
    if not redSum or not blueSum: return INF
    #인접한곳 돌면서 지워줌
    while rq:
        x = rq.popleft()
        red &= ~(1<<x)
        for nx in adj[x]:
            if red & (1<<nx) and picked & (1<<nx):
                rq.append(nx)
    while bq:
        x = bq.popleft()
        blue &= ~(1<<x)
        for nx in adj[x]:
            if blue & (1<<nx) and not (picked & (1<<nx)):
                bq.append(nx)
    #도달 못해서 지우지 못한곳 있으면 INF 
    if red or blue: return INF
    return abs(redSum-blueSum)
    
    
def solve(pos, picked):
    res=INF
    if pos == n: return bfs(picked)
    #선택하거나 선택안하거나, 완탐 O(2**n)
    res = min(res, solve(pos+1, picked), solve(pos+1, picked|(1<<pos)))
    return res

n=int(input())
INF=1e9
popul = list(map(int,input().split()))
adj=[[]for _ in range(n)]
for i in range(n):
    temp = list(map(int,input().split()))
    for x in temp[1:]:
        x-=1
        adj[i].append(x)
res = solve(0, 0)
print(res if res != INF else -1)
