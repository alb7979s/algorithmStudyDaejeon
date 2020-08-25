import sys
sys.stdin = open('1767_input.txt')

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 프로세서 연결하기
def runProcessor(pr, pc, d, depth):
    cnt = 0
    while True:
        pr += dr[d]
        pc += dc[d]
        if not (0 <= pr < N and 0 <= pc < N):   # 전원 만나면 길이 리턴
            return cnt
        if raw[pr][pc]:     # 길 막혔으면 길이 0 리턴
            return 0
        cnt += 1
        raw[pr][pc] = 10 + depth

# 연결한 전선 지우기
def cleanLine(pr, pc, d, depth):
    while True:
        pr += dr[d]
        pc += dc[d]
        if not (0 <= pr < N and 0 <= pc < N):
            return
        if raw[pr][pc] != 10 + depth:
            return
        raw[pr][pc] = 0

# 연결 확인한 코어, 현재 전선의 길이, 실제 연결한 코어의 수
def dfs(depth, length, K):
    global minLength, maxCore, N, count
    if depth == count:
        if K == maxCore:
            minLength = min(minLength, length)
        elif K > maxCore:
            maxCore = K
            minLength = length
        return

    r, c = cores[depth]
    for i in range(4):       # 같은 depth에서 4방향 탐색
        lineCount = runProcessor(r, c, i, depth)
        if lineCount:        # 전원에 연결하면 다음 코어 연결 시도
            dfs(depth+1, length+lineCount, K+1)
        cleanLine(r, c, i, depth)   # 연결선 제거
    dfs(depth+1, length, K)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    maxCore = float('-inf')
    minLength = float('inf')

    cores = []
    count = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if raw[i][j]:
                cores.append((i, j))
                count += 1

    dfs(0, 0, 0)
    print("#{} {}".format(tc+1, minLength))