import sys
sys.stdin = open('2383_input.txt')

def solve(selected):
    global result
    waiting = [[], []]    # 계단별로 사람들이 입구 도착할 때까지 걸린 시간
    for i in range(P):
        stairNum = selected[i]
        pr, pc = person[i]          # 사람 위치
        sr, sc = stairs[stairNum]   # 선택한 계단의 좌표
        time = abs(pr-sr) + abs(pc-sc) + 1
        waiting[stairNum].append(time)
    # print(waiting)

    second = 0
    stair = [[], []]    # 계단 내려가는 사람들이 완전히 나갈 수 있는 시간 저장
    # 모든 사람이 계단을 완전히 빠져나갈 때까지
    while len(max(*stair)) + len(max(*waiting)):
        second += 1             # 시간 흐름
        if second >= result:    # 가지치기
            return

        for i in range(2):      # 계단별로 작업 처리
            for s in reversed(range(len(stair[i]))):
                if second >= stair[i][s]:
                    stair[i].pop(s)
            for w in reversed(range(len(waiting[i]))):
                if len(stair[i]) < 3 and second >= waiting[i][w]:
                    waiting[i].pop(w)
                    sr, sc = stairs[i]
                    stair[i].append(second + A[sr][sc])
    result = min(result, second)

def comb(depth):
    if depth == P:
        # print(select)
        solve(select)
        return
    for i in range(2):
        select.append(i)
        comb(depth+1)
        select.pop()

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    P = 0
    stairs, person = [], []
    for i in range(N):
        for j in range(N):
            if A[i][j] > 1:
                stairs.append((i, j))
            elif A[i][j] == 1:
                person.append((i, j))
                P += 1
    select = []
    comb(0)
    print("#{} {}".format(tc+1, result))