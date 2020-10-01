def move(sx, sy):
    global a, fish
    for i in range(1, 17):
        if fish[i]:
            x, y = fish[i]
            f, d = a[x][y]
            for j in range(8):
                nd = (j+d)%8
                dx, dy = dd[nd]
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>3 or ny>3 or (nx==sx and ny==sy): continue
                fish[i] = (nx, ny)
                if not a[nx][ny]:
                    a[x][y] = 0
                else:
                    fn, fd = a[nx][ny]
                    a[x][y] = [fn, fd]
                    fish[fn] = (x, y)
                a[nx][ny] = [i, nd]
                break
def solve(x, y, score, d):
    global a, fish
    res = 0
    move(x, y)
    fish2 = [x for x in fish]
    a2 = [x[:] for x in a]
    dx, dy = dd[d]
    isContinue = False
    while 1:
        x, y = x+dx, y+dy
        if x<0 or y<0 or x>3 or y>3:break
        if not a[x][y]: continue
        isContinue = True
        f, fd = a[x][y]
        a[x][y]=0
        fish[f]=0
        res = max(res, solve(x, y, score+f, fd))
        a = [x[:] for x in a2]
        fish = [x for x in fish2]
    if isContinue: return res
    return score
fish=[0]*17
a=[[]for _ in range(4)]
dd=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
for i in range(4):
    b = list(map(int,input().split()))
    for j in range(4):
        f, d = b[j*2], b[j*2+1]
        fish[f] = (i, j)
        a[i].append([f,d-1])
f, d = a[0][0]
fish[f]=0
a[0][0]=0
print(solve(0, 0, f, d))
