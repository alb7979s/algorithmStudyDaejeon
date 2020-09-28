from collections import*
dd=[(0.5, 0), (-0.5, 0), (0, -0.5), (0, 0.5)]
for tc in range(int(input())):
    n=int(input())
    q=deque()
    for i in range(n):
        y, x, d, k = map(int,input().split())
        q.append((x, y, d, k))
    #dict()에 [x][y]=[d, k]
    res = 0
    for i in range(4002):
        a={}
        while q:
            x, y, d, k = q.popleft()
            nx, ny = x+dd[d][0], y+dd[d][1]
            if (nx, ny) not in a:
                a[nx, ny] = [d, k]
            else:
                a[nx, ny][0] = -1
                a[nx, ny][1] += k
        for (x, y), (d, k) in a.items():
            if d==-1:
                res += k
            else:q.append((x, y, d, k))
        if not q: break
    print('#{} {}'.format(tc+1, res))
