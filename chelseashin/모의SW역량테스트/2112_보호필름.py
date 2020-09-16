import sys
sys.stdin = open('2112_input.txt')

# 성능 테스트
def test(F):
    check = 0
    for c in range(W):
        cnt = 1
        temp = F[0][c]
        for r in range(1, D):
            if F[r][c] == temp:
                cnt += 1
            else:
                temp = F[r][c]
                cnt = 1
            if cnt >= K:
                check += 1
                break
        if (c+1) != check:
            return False
    return True

# 현재 약물 투입 횟수, 시작 행 위치, 최대 투입 횟수
def dfs(depth, pos, K):
    global MIN
    if depth >= MIN:    # 가지치기
        return
    if depth == K:
        if test(film):
            MIN = min(MIN, depth)
        return
    for i in range(pos, D):     # 약물 투입할 행 선택
        for j in range(2):
            if selected[i]:
                continue
            selected[i] = 1
            film[i] = drug[j]   # 약품 투입
            dfs(depth+1, i+1, K)
            film[i] = raw[i]    # 복원
            selected[i] = 0

# main
T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    film = [r[:] for r in raw]
    drug = [[0] * W, [1] * W]
    selected = [0] * D
    MIN = float('inf')

    if test(film):
        MIN = 0
    else:
        for i in range(1, K+1):  # 약물 투여 최대 횟수 K까지 할 수 있음
            dfs(0, 0, i)

    print("#{} {}".format(tc + 1, MIN))