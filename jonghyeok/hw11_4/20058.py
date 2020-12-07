from sys import*
input=stdin.readline
from collections import*
def bfs(x, y):
    global res
    visit[x][y]=1
    res += board[x][y]
    cnt = 1
    q=deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or visit[nx][ny] or not board[nx][ny]: continue
            res += board[nx][ny]
            visit[nx][ny]=1
            cnt += 1
            q.append((nx, ny))
    return cnt
N, K = map(int,input().split())
n = 1 << N
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
L = list(map(int,input().split()))
for l in L:
    l = 1<<l
    zeros = [[1]*(n+2) for _ in range(n+2)]
    for sx in range(0, n, l):
        for sy in range(0, n, l):
            #여기서 90도 회전 해줘야함
            temp = [[0]*l for _ in range(l)]
            for i in range(l):
                for j in range(l):
                    temp[j][l-i-1] = board[i+sx][j+sy]
            for i in range(l):
                for j in range(l):
                    board[sx+i][sy+j] = temp[i][j]
                    if temp[i][j]: zeros[sx+i+1][sy+j+1]=0
    #n * n 돌면서 주위 0이하 두개이상인곳 체크
    for i in range(n):
        for j in range(n):
            if board[i][j] and (zeros[i][j+1] + zeros[i+1][j+2] + zeros[i+1][j] + zeros[i+2][j+1])>=2: board[i][j]-=1
#마지막 n*n 돌면서 BFS cnt 가장 큰거 구하고(그냥 전역변수로 구해도 됨), 전역변수로 sum 구하기
visit = [[0]*n for _ in range(n)]
res = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j] and board[i][j]:
            cnt = max(cnt, bfs(i, j))
print(res, cnt, sep='\n')
