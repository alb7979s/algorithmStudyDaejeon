import sys
sys.stdin = open('19237_input.txt')
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def solve():
    time = 0
    cnt = 0
    while True:
        time += 1
        if time > 1000:
            print(-1)
            return
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(M):  # 상어별 처리
            if shark[i]:
                r, c, d = shark[i]
                # 우선순위 1 : 이동할 수 있는 빈 칸 있는지 여부
                flag = 0
                for nd in shark_dir[i][d - 1]:
                    nr = r + dr[nd - 1]
                    nc = c + dc[nd - 1]
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if not A[nr][nc]:  # 빈 공간 발견
                        flag = 1
                        break
                # 우선순위 2 : 빈 공간 발견하지 못하면 나와 같은 냄새 있는 곳으로
                if not flag:
                    for nd in shark_dir[i][d - 1]:
                        nr = r + dr[nd - 1]
                        nc = c + dc[nd - 1]
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        if A[nr][nc][0] == i + 1:  # 같은 번호의 냄새
                            break
                # 값 없으면 등록
                if not visited[nr][nc]:
                    visited[nr][nc] = i + 1  # 번호 등록
                    shark[i] = [nr, nc, nd]
                # 값이 있으면 나보다 번호 큰지 작은지 검사
                else:
                    # 원래 있던 상어 번호가 현재 번호보다 작으면
                    if visited[nr][nc] < i + 1:
                        cnt += 1
                        shark[i] = 0  # 현재 상어 쫓겨남(0으로 바꿈)
                    else:  # 그렇지 않으면 원래 있던 상어 쫓겨남
                        shark[visited[nr][nc] - 1] = 0
                        cnt += 1
                        visited[nr][nc] = i + 1
        if cnt == M-1:
            print(time)
            return
        # 원래 있던 상어 냄새 1 감소
        for r in range(N):
            for c in range(N):
                if A[r][c]:
                    A[r][c][1] -= 1
                    if A[r][c][1] == 0:
                        A[r][c] = 0  # 빈 칸으로 만들기
        # 새 상어 맵에 표시
        for i in range(M):
            if shark[i]:
                r, c = shark[i][0], shark[i][1]
                A[r][c] = [i + 1, K]

# main
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
shark = [[] for _ in range(M)]
for i in range(N):
    for j in range(N):
        if A[i][j]:
            # 상어의 번호별 좌표, 현재방향 표시
            shark[A[i][j] - 1] = [i, j, direction[A[i][j] - 1]]
            A[i][j] = [A[i][j], K]  # 맵에 상어 번호와 남은 냄새 시간 표시

# 상어 이동방향 우선순위 정보
shark_dir = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

solve()