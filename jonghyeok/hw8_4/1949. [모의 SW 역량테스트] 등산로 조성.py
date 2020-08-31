def dfs(x,y,c):
    f=0
    res=0
    for dx, dy in dd:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or check[nx][ny] or a[nx][ny] >= a[x][y]:continue
        check[nx][ny]=1
        f = 1
        res=max(res, dfs(nx,ny,c+1))
        check[nx][ny]=0
    if not f:
        return c
    return res

dd=[(-1,0),(1,0),(0,-1),(0,1)]
for tc in range(int(input())):
    n, k = map(int,input().split())
    a=[]
    top=0
    for i in range(n):
        a.append(list(map(int,input().split())))
        top=max(top, max(a[i]))
    top_list=[]
    #가장 높은 값들 저장
    for i in range(n):
        for j in range(n):
            if a[i][j]==top:
                top_list.append((i,j))
    res=0
    check = [[0] * n for _ in range(n)]
    #모든 지형에 대해서
    for i in range(n):
        for j in range(n):
            #k만큼 깎을 수 있음
            for m in range(k + 1):
                temp = a[i][j]
                a[i][j] -= m
                #지형 음수는 안되나벼 fail뜸
                if a[i][j] < 0: a[i][j] = 0
                #깎았으면 가장 높은 봉우리들에 대해서 dfs 실행
                for x, y in top_list:
                    check[x][y] = 1
                    res = max(res, dfs(x, y, 1))
                    check[x][y] = 0
                #깎은거 원래대로
                a[i][j] = temp
    print('#{} {}'.format(tc+1,res))
