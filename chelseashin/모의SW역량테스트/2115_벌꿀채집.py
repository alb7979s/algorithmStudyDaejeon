import sys
sys.stdin = open('2115_input.txt')
from itertools import combinations

def check(L):
    res = 0
    if sum(L) == C:     # 해당 범위의 합이 채취할 수 있는 최대양인 경우
        for n in L:
            res += n ** 2
        return res
    res = max(L) ** 2   # 최대값을 해당 범위 내 가장 큰 값의 제곱으로 함
    for s in range(2, M+1):
        for comb in combinations(L, s):
            if sum(comb) > C:
                continue
            temp = 0
            for n in comb:
                temp += n ** 2
            res = max(res, temp)    # 최대값 갱신
    return res

def dfs(depth, start):
    global MAX
    if depth == 2:
        a, b = [], []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    a.append(A[i][j])
                elif visited[i][j] == 2:
                    b.append(A[i][j])
        MAX = max(MAX, check(a) + check(b))
        return
    for r in range(start, N):
        for c in range(N-M+1):
            flag = True
            for d in range(M):
                if visited[r][c+d]:
                    flag = False
                    break
            if flag:    # 범위 차지할 수 있으면
                for d in range(M):
                    visited[r][c+d] = depth+1
                dfs(depth+1, r)
                for d in range(M):
                    visited[r][c+d] = 0

# main
T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    MAX = float('-inf')
    visited = [[0] * N for _ in range(N)]
    dfs(0, 0)
    print("#{} {}".format(tc+1, MAX))

    # 1 174
    # 2 131
    # 3 145
    # 4 155
    # 5 166
    # 6 239
    # 7 166
    # 8 172
    # 9 291
    # 10 464