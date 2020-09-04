from sys import*
input=stdin.readline
dd=[(0,1),(-1,0),(0,-1),(1,0)]  #RULD
n=int(input())
a=[[0]*101 for _ in range(101)]
for draw in range(n):
    y, x, d, g = map(int,input().split())
    v = []
    v.append(d)
    for i in range(g):
        lv = len(v)
        for j in range(lv-1, -1, -1):
            v.append((v[j]+1)%4)
    a[x][y]=1
    for d in v:
        dx, dy = dd[d]
        x, y = x+dx, y+dy
        a[x][y]=1
cnt=0
for i in range(100):
    for j in range(100):
        if a[i][j] and a[i][j+1] and a[i+1][j] and a[i+1][j+1]: cnt+=1
print(cnt)
