import sys
sys.stdin = open('17070_input.txt')

def dfs(sr, sc, dir):
    global A, cnt
    if sr == N-1 and sc == N-1:
        cnt += 1
        return
    # 가로 방향
    if dir == 1:
        if sc+1 < N and A[sr][sc+1] == 0:
            dfs(sr, sc+1, 1)
        if sr+1 < N and sc+1 < N and A[sr+1][sc] == 0 and A[sr][sc+1] == 0 and A[sr+1][sc+1] == 0:
            dfs(sr+1, sc+1, 3)
    # 세로 방향
    elif dir == 2:
        if sr+1 < N and A[sr+1][sc] == 0:
            dfs(sr+1, sc, 2)
        if sr+1 < N and sc+1 < N and A[sr+1][sc] == 0 and A[sr][sc+1] == 0 and A[sr+1][sc+1] == 0:
            dfs(sr+1, sc+1, 3)
    # 대각선 방향
    elif dir == 3:
        if sc+1 < N and A[sr][sc+1] == 0:
            dfs(sr, sc+1, 1)
        if sr+1 < N and A[sr+1][sc] == 0:
            dfs(sr+1, sc, 2)
        if sc+1 < N and sr+1 < N and A[sr+1][sc] == 0 and A[sr][sc+1] == 0 and A[sr+1][sc+1] == 0:
            dfs(sr+1, sc+1, 3)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 1)
print(cnt)