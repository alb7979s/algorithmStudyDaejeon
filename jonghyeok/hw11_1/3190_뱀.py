from sys import*
from collections import*
input=stdin.readline
dd=[(0, 1), (1, 0), (0, -1), (-1, 0)]   #RDLU
n=int(input())
arr = [[0]*n for _ in range(n)]
turns = []
for i in range(int(input())):
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1   #1이 사과
L = int(input())
for i in range(L):
    turns.append(list(map(str,input().split())))
x, y, t, d, turnIdx = 0, 0, 0, 0, 0
tail = deque()
arr[x][y]=2
while 1:
    t+=1
    tail.append((x, y))
    dx, dy = dd[d]
    x, y = x+dx, y+dy
    if x<0 or y<0 or x>n-1 or y>n-1 or arr[x][y]==2:    #벽에 닿거나 자기 몸에 닿으면 종료
        print(t)
        break
    if arr[x][y]==1:                                    #사과면 먹음
        pass
    else:                                               #빈칸이면 꼬리 한칸 제거
        tx, ty = tail.popleft()
        arr[tx][ty]=0
    arr[x][y]=2
    if turnIdx<L and int(turns[turnIdx][0]) == t:
        if turns[turnIdx][1] == 'D':
            d = (d+1)%4
        else:
            d = (d+3)%4
        turnIdx+=1
