import sys
sys.stdin = open('19236_input.txt')
input = sys.stdin.readline
# from copy import deepcopy

# 성공 풀이
# Simulation + Brute Force(DFS)
# 상어가 먹을 수 있는 물고기 번호의 최대값 구하기
# 즉, 모든 경우에 대해서 끝까지 진행하고 최종적으로 판단해야 함

# 8방향
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)

# 맵에서 해당 번호의 물고기 위치 리턴
def find_fish(idx, A):
    for i in range(4):
        for j in range(4):
            if A[i][j] and A[i][j][0] == idx:
                # 위치 정보, 방향 리턴
                return [i, j, A[i][j][1]]
    return 0

# 물고기 이동
def fish_move(A, sr, sc):
    for i in range(1, 17):
        pos = find_fish(i, A)
        if not pos:
            continue
        r, c, d = pos   # 해당 물고기의 위치와 방향
        for j in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 4 and 0 <= nc < 4):   # 맵 벗어나거나
                d = (d+1) % 8
                continue
            if nr == sr and nc == sc:   # 상어 있는 위치면 방향 전환
                d = (d+1) % 8
                continue
            # 빈 칸, 상어가 있는 위치였던 곳, 물고기가 있는 경우면 모두 가능
            A[r][c][0], A[nr][nc][0] = A[nr][nc][0], A[r][c][0]
            A[r][c][1], A[nr][nc][1] = A[nr][nc][1], d
            break

# 상어가 이동할 수 있는 좌표 리스트 리턴
def shark_move(A, r, c):
    candidates = []
    dir = A[r][c][1]        # 상어의 이동방향
    for i in range(4):
        nr = r + dr[dir] * i
        nc = c + dc[dir] * i
        if not (0 <= nr < 4 and 0 <= nc < 4):   # 맵 벗어나거나
            continue
        if not (1 <= A[nr][nc][0] <= 16):   # 먹을 물고기 없으면
            continue
        candidates.append([nr, nc])
    return candidates

# 현재 배열, 상어의 위치, 먹은 물고기 번호의 합
def dfs(A, r, c, total):
    global result
    # 배열 복사해놓기
    arr = [[A[i][j][:] for j in range(4)] for i in range(4)]
    # arr = deepcopy(A)

    # 상어는 해당 위치의 물고기 먹고 그 위치로 이동
    eat = arr[r][c][0]
    arr[r][c][0] = -1

    # 물고기 먹을 때마다 최댓값 갱신
    result = max(result, total + eat)

    # 물고기 이동(맵과 상어의 위치 넘기기)
    fish_move(arr, r, c)
    
    # 상어 이동할 수 있는 좌표 후보 담기(맵과 상어의 위치 넘기기)
    ways = shark_move(arr, r, c)

    for nr, nc in ways:
        dfs(arr, nr, nc, total+eat)
        A = [x[:] for x in arr]     # 배열 되돌리기

# main
raw = [[] for _ in range(4)]
for i in range(4):
    L = list(map(int, input().split()))
    for j in range(0, 7, 2):
        raw[i].append([L[j], L[j+1]-1])

shark = raw[0][0]
result = float('-inf')
dfs(raw, 0, 0, 0)
print(result)