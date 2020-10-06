import sys
sys.stdin = open('4012_input.txt')

def synergy(S):
    each = [0, 0]
    for i in range(N):
        for j in range(N):
            if S[i] == S[j]:
                each[S[i]] += flavor[i][j]
    return abs(each[0] - each[1])


# def comb(depth, k):
#     if depth == N//2:
#         print(selected)
#         return
#     # if k == N//2:
#         # print(selected)
#         # MIN = min(MIN, synergy(selected))
#         # return
#     for i in range(k, N):
#         selected[i] = 1
#         comb(depth + 1, i+1)
#         selected[i] = 0

def comb(depth, k):
    global MIN
    if MIN == 0:
        return
    if depth == N:
        print(selected)
        MIN = min(MIN, synergy(selected))
        return
    if k == N//2:
        # print(selected)
        # MIN = min(MIN, synergy(selected))
        return
    selected[depth] = 1
    comb(depth + 1, k+1)
    selected[depth] = 0
    comb(depth + 1, k)

T = int(input())
for tc in range(T):
    N = int(input())
    flavor = [list(map(int, input().split())) for _ in range(N)]
    MIN = float('inf')
    selected = [0] * N
    comb(0, 0)
    print("#{} {}".format(tc+1, MIN))

    # 1 2
    # 2 1
    # 3 38
    # 4 15
    # 5 4
    # 6 0
    # 7 51
    # 8 23
    # 9 13
    # 10 11