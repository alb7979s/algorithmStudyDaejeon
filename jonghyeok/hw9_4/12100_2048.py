from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def move(x, y, dx, dy):
    global res, a
    q=deque()
    idx = 0
    nx, ny = x, y
    for i in range(n):
        if a[nx][ny]:
            if len(q) <= idx:
                q.append(a[nx][ny])
            else:
                #같으면 두배 아니면 그냥 추가
                if q[idx] == a[nx][ny]:
                    q[idx] *= 2
                    res = max(res, q[idx])
                else:
                    q.append(a[nx][ny])
                idx+=1
            a[nx][ny]=0
        nx, ny = nx+dx, ny+dy
    while q:
        a[x][y] = q.popleft()
        x, y = x+dx, y+dy
def solve(pos):
    global a
    if pos == 5: return
    b = [x[:] for x in a]
    for i in range(4):
        for j in range(n):  #한 행 or 한 열씩 움직임
            if i==0: move(j, 0, 0, 1)
            elif i==1: move(n-1, j, -1, 0)
            elif i==2: move(j, n-1, 0, -1)
            else: move(0, j, 1, 0)
        solve(pos+1)
        a = [x[:] for x in b]
    return
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
res = 0
for i in range(n):
    res = max(res, max(a[i]))
solve(0)
print(res)
