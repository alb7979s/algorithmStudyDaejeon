from collections import*
U, R, D, L = 1, 2, 4, 8
dd = [(-1,0), (0,1), (1,0), (0,-1)] #집합일땐 (1<<i), 그냥 방향 참조땐 i
IN = [0,          #입구
      U|R|D|L,    #1
      U|D,        #2
      L|R,        #3
      D|L,        #4
      L|U,        #5
      R|U,        #6
      R|D]        #7
OUT = [0,         #출구
       U|R|D|L,
       U|D,
       L|R,
       U|R,
       R|D,
       L|D,
       U|L]
for tc in range(int(input())):
    n, m, r, c, l = map(int,input().split())
    a = [list(map(int,input().split()))for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    q=deque()
    cnt=1
    for i in range(4):      #나갈 수 있는곳 큐에 넣음
        if OUT[a[r][c]] & (1<<i):
            q.append((r, c, i))
    check[r][c]=1
    #l시간동안 움직임(처음 시작이 1시간이라 l-1만큼만 퍼뜨림)
    for _ in range(l-1):
        lq = len(q)
        for i in range(lq):
            x, y, d = q.popleft()
            dx, dy = dd[d]
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or check[nx][ny]: continue
            #나갈 수 있는 방향 d로 들어갈 수 있는 곳이 있으면
            if IN[a[nx][ny]] & (1 << d):
                check[nx][ny] = 1
                cnt += 1
                #그 곳에서 나갈 수 있는 방향 모두 큐에 넣어줌
                for j in range(4):
                    if OUT[a[nx][ny]] & (1 << j):
                        q.append((nx, ny, j))
    print('#{} {}'.format(tc + 1, cnt))
