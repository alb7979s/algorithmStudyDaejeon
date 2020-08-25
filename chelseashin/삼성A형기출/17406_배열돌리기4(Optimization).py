import sys
sys.stdin = open('17406_input.txt')

# Optimization

from itertools import permutations

# 우, 하, 좌, 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# 배열 넣었을 때 행별 최솟값 구하기
def check(arr):
    global MIN
    for i in range(N):
        temp = sum(arr[i])
        if MIN > temp:
            MIN = temp
    return

def rotate(order):
    A = [x[:] for x in raw]
    for cal in order:
        # 왼쪽 상단 좌표, 오른쪽 하단 좌표 저장
        sr, sc = cal[0] - cal[2], cal[1] - cal[2]
        er, ec = cal[0] + cal[2], cal[1] + cal[2]
        # print(sr, sc, er, ec)
        while True:
            # 종료조건 : 시작점, 끝점 위치 만나면 break
            if sr >= er and sc >= ec:
                break
            dir = 0
            r, c, prev = sr, sc, A[sr][sc]
            while True:
                nr = r + dr[dir]
                nc = c + dc[dir]
                if not (sr <= nr <= er and sc <= nc <= ec):  # 범위 벗어나면
                    dir += 1  # 방향 바꾸기
                    continue
                prev, A[nr][nc] = A[nr][nc], prev
                r, c = nr, nc
                # 한 바퀴 돌아서 시작점까지 왔을 때
                if r == sr and c == sc:
                    sr += 1
                    sc += 1
                    er -= 1
                    ec -= 1
                    break
    # print(A)
    check(A)
    return


N, M, K = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

calList = []
for _ in range(K):
    r, c, s = map(int, input().split())
    calList.append([r-1, c-1, s])
# 연산 순서 정하기
for perm in list(permutations(calList, K)):
    rotate(perm)
print(MIN)