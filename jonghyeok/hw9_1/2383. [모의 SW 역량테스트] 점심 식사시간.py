import sys
from collections import*
sys.stdin = open('C:/projects/mysite/algorithms/test.txt')
INF = 1e9
def cal():
    # s[0] stairs 첫 번째 시간들 s[1] 두 번째 시간들
    res = -INF
    for i in range(2):
        temp = sorted(s[i])
        q=deque()
        t = 0
        pos = 0
        while 1:
            #계단 다 내려왔으면 빼줌
            while q:
                if q[0] <= t: q.popleft()
                else: break
            #계단 최대 세명, pos 여유 있으면, 도착한 시각이 t보다 빠르거나 같으면
            while len(q)<3 and pos < len(temp) and temp[pos] < t:
                #내려가야 하는 길이의 시간 + 현재 시각, 대기하던건 1 추가 안해도됨!!
                q.append(sl[i]+t)
                pos+=1
            if pos == len(temp) and not q: break
            t+=1
        res = max(res, t)
    return res
def solve(pos):
    global s
    res = INF
    if pos == len(man):
        res = min(res, cal())
        return res
    mx, my = man[pos]
    for i in range(2):
        sx, sy = stairs[i]
        s[i].append(abs(sx-mx)+abs(sy-my))
        res = min(res, solve(pos+1))
        s[i].pop()
    return res
for tc in range(int(input())):
    global s
    n=int(input())
    man = []
    stairs = []
    s = [[]for _ in range(2)]
    sl = []
    a=[list(map(int,input().split()))for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j]==1: man.append((i, j))
            elif a[i][j]:
                stairs.append((i, j))
                sl.append(a[i][j])
    print('#{} {}'.format(tc+1, solve(0)))
