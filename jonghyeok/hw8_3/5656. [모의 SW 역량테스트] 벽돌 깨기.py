#k번 벽돌 뽀개고 남은 벽돌 개수의 최소값
def gravity(check):
    #check 얻은 정보로 터뜨리기
    fire=0
    for i in range(n):
        for j in range(m):
            if check[i][j] and a[i][j]:
                a[i][j]=0
                fire+=1
    #중력
    for i in range(m):
        temp=[]
        for j in range(n):
            if a[j][i]:
                temp.append(a[j][i])
                a[j][i]=0
        loc=n-1
        while temp:
            a[loc][i]=temp.pop()
            loc-=1
    return fire
def remove(x, y, l, check): #지우는 함수
    check[x][y]=1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for i in range(1, l):
            nx, ny = x+dx*i, y+dy*i
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or check[nx][ny] or not a[nx][ny]: continue
            remove(nx, ny, a[nx][ny], check)
def solve(cnt, bricks):     #터뜨리는곳 정하는 함수
    global a
    res=INF
    if not bricks or cnt == k:
        return bricks
    b = [x[:] for x in a]
    for i in range(m):
        for j in range(n):
            if a[j][i]:
                check=[[0]*m for _ in range(n)]
                remove(j, i, a[j][i], check)
                res = min(res, solve(cnt+1, bricks-gravity(check)))
                a = [x[:] for x in b]
                break       #주의!! 끝내줘야함
    return res
INF=int(1e9)
for tc in range(int(input())):
    k,m,n=map(int,input().split())
    a=[]
    b=0
    for i in range(n):
        a.append(list(map(int,input().split())))
        for j in range(m):
            if a[i][j]:b+=1
    print('#{} {}'.format(tc+1, solve(0, b)))
