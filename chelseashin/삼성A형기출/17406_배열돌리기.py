import sys
sys.stdin = open('17406_input.txt')

# 1. 입력하는 연산을 [r, c, s] 배열에 저장한다.
# 2. dfs로 순열을 구현하여 연산 순서를 정한다
# 3. rotate에서 회전을 구현한다. 왼쪽 상단좌표는 sr, sc, 오른쪽 하단좌표는 er, ec로 저장한다
# 4. a[sr][sc]값을 before에 저장하고 한 칸씩 이동하면서 현재값을 before로 바꾸고 before을 갱신한다
# 5. 범위를 벗어날 때마다 방향을 바꿔준다
# 6. sr, sc 좌표에 위치하게 되면 sr와 sc에 1을 더하고 er와 ec에 1을 빼서 회전할 범위를 좁혀준다
# 7. 회전할 수 있을 때 까지 반복한다. sr이 er보다 크거나 sc가 ec보다 크면 중단한다
# 8. row의 합 중에서 최소값을 temp에 저장하고 MIN을 계산한다
# 9. 순열의 모든 경우를 확인한 후 MIN를 출력

from copy import deepcopy
from collections import deque

# 우, 하, 좌, 상(시계방향 돌리기 위해)
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

def dfs(depth):
    if depth == K:
        Q2 = deepcopy(Q)
        rotate(Q2)
        return
    for i in range(K):
        if visited[i]:
            continue
        visited[i] = 1
        Q.append(calList[i])
        dfs(depth + 1)
        Q.pop()
        visited[i] = 0

def rotate(Q):
    A = deepcopy(raw)
    # 큐에 값 있는 동안(연산 갯수 만큼)
    while Q:
        r, c, s = Q.popleft()
        # 왼쪽 상단 좌표, 오른쪽 하단 좌표 저장
        sr, sc, er, ec = r-s, c-s, r+s, c+s
        while True:
            # 시작점, 끝점 위치 만나면 break
            if sr >= er or sc >= ec:
                break
            dir = 0    # 방향변수
            r, c, before = sr, sc, A[sr][sc]    # 시작 위치와 값 저장
            # 가장 큰 둘레부터 달팽이 모양으로 돌리기
            while True:
                nr = r + dr[dir]
                nc = c + dc[dir]
                if not (sr <= nr <= er and sc <= nc <= ec):  # 범위 벗어나면
                    dir += 1    # 방향 바꾸기
                    continue
                temp = A[nr][nc]
                A[nr][nc] = before
                before = temp
                r, c = nr, nc
                # 한 바퀴 돌아서 시작점까지 왔을 때
                if r == sr and c == sc:
                    sr += 1
                    sc += 1
                    er -= 1
                    ec -= 1
                    break
        # print(A)  # 돌렸을 때 상태 확인
    check(A)
    return

N, M, K = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')
calList = []
for _ in range(K):
    r, c, s = map(int, input().split())
    calList.append([r-1, c-1, s])

visited = [0] * K
Q = deque()
dfs(0)
print(MIN)