from collections import*
# import sys
# sys.stdin = open('test.txt')
def bfs(x, y, c, p, idx):
    global info
    q=deque()
    q.append((x, y))
    visit=[[0]*n for _ in range(n)]
    visit[x][y]=1
    for i in range(c):
        lq = len(q)
        for j in range(lq):
            x, y = q.popleft()
            for dx, dy in dd:
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny]:continue
                info[nx][ny].append((p, idx))
                visit[nx][ny]=1
                q.append((nx, ny))
dd=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]
for tc in range(int(input())):
    global n, info
    n = 10
    m, k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    info = [[[]for _ in range(n)] for _ in range(n)]
    for i in range(k):
        y, x, c, p = map(int,input().split())
        x-=1; y-=1
        info[x][y].append((p, i))
        bfs(x, y, c, p, i)
    for i in range(n):
        for j in range(n):
            info[i][j].sort(reverse=True)
    ax, ay = 0, 0
    bx, by = 9, 9
    res=0
    for i in range(m+1):
        #a없고 b있으면 b만 더함
        if not info[ax][ay]:
            if info[bx][by]:
                res += info[bx][by][0][0]
        #a있고 b없으면 a만 더함
        elif not info[bx][by]:
            res += info[ax][ay][0][0]
        #a, b 가장 큰 충전량의 번호가 다르면 가장큰거 두개 더함
        elif info[ax][ay][0][1] != info[bx][by][0][1]:
            res += info[ax][ay][0][0] + info[bx][by][0][0]
        #a, b 둘 다 있는데 가장 큰 충전량 번호가 같으면 중복되는거임,
        #두 개 이상 있는 곳 중 최대값이랑 충전량 가장 큰거 더해줘야함, 둘 다 하나면 중복되는거라 (a+a)/2 = a임 그냥 처음 원소만 더해주면됨
        #tmep=0으로 해주고 원소 있으면 갱신해주는 식으로 처리함
        else:
            temp = 0
            if len(info[ax][ay])>1: temp = info[ax][ay][1][0]
            if len(info[bx][by])>1: temp = max(temp, info[bx][by][1][0])
            res += info[ax][ay][0][0]+temp
        if i == m: break
        dx, dy = dd[a[i]]
        ax, ay = ax+dx, ay+dy
        dx, dy = dd[b[i]]
        bx, by = bx+dx, by+dy
        # print(res, ax, ay, bx, by
    print('#{} {}'.format(tc+1, res))
