import sys
sys.stdin = open('1966_input.txt')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    # print(N, M, L)
    Q = [(i, v) for i, v in enumerate(L)]

    order = 0
    while True:
        if Q[0][1] == max([v for i, v in Q]):
            order += 1

            if Q[0][0] == M:
                print(order)
                break
            else:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
        # print(Q)