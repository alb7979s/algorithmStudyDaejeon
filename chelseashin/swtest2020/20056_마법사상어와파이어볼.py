import sys
sys.stdin = open("20056_input.txt")
from collections import deque

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

# 홀짝 여부 확인
def check(L):
    temp = 0
    for t in L:
        temp += t % 2
    if temp == 0 or temp == len(L):
        return True
    return False

# main
N, M, K = map(int, input().split())
Q = deque()
for _ in range(M):
    # 파이어볼의 위치 (r, c), 질량 m, 속력 s, 방향 d
    r, c, m, s, d = map(int, input().split())
    Q.append((r-1, c-1, m, s, d))

for k in range(K):
    # 1. 파이어볼 이동
    D = {}
    qlen = len(Q)
    for _ in range(qlen):
        r, c, m, s, d = Q.popleft()
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        if (nr, nc) not in D.keys():
            D[(nr, nc)] = [[m, s, d]]
        else:
            D[(nr, nc)].append([m, s, d])
    for key, value in D.items():
        tr, tc = key
        vlen = len(value)
        if vlen == 1:
            tm, ts, td = value[0]
            Q.append((tr, tc, tm, ts, td))
        # 2. 2개 이상의 파이어볼이 있는 칸
        else:
            tm, ts = 0, 0
            td = []
            for n in range(vlen):
                tm += value[n][0]
                ts += value[n][1]
                td.append(value[n][2])
            tm //= 5        # 질량
            ts //= vlen     # 속력
            if tm <= 0:     # 질량 0보다 작으면 소멸
                continue
            if check(td):   # 홀짝 확인 후 방향 정하기
                dir = [0, 2, 4, 6]
            else:
                dir = [1, 3, 5, 7]
            if tm > 0:   # 질량이 0보다 크면 나눠짐
                for dd in dir:
                    Q.append((tr, tc, tm, ts, dd))
# 남은 질량의 총합
result = 0
for qvalue in Q:
    result += qvalue[2]
print(result)