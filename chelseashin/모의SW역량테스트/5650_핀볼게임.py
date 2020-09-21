import sys
sys.stdin = open('5650_input.txt')

# 시뮬레이션 문제

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 방향 전환
change = [(),
          (1, 3, 0, 2),
          (3, 0, 1, 2),
          (2, 0, 3, 1),
          (1, 2, 3, 0),
          (1, 0, 3, 2)]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    B = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]

    wormhole = {}   # 웜홀 같은 번호끼리 쌍으로 저장(딕셔너리)
    check = [0] * 11   # 0 ~ 5는 의미X, 6 ~ 10 wormhole 방문체크
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 6 <= B[i][j] <= 10:
                worm_start = check[B[i][j]]
                if not worm_start:
                    check[B[i][j]] = (i, j)
                else:
                    wormhole[worm_start] = (i, j)
                    wormhole[(i, j)] = worm_start
    # print(wormhole)

    result = float('-inf')
    for r in range(1, N+1):
        for c in range(1, N+1):
            if B[r][c] == 0:        # 모든 0이 시작 가능한 점, 시작 점 저장
                for d in range(4):  # 4방향 탐색
                    score = 0
                    nr = r + dr[d]
                    nc = c + dc[d]
                    while True:
                        # 시작점이거나 블랙홀이면 종료
                        if (nr == r and nc == c) or B[nr][nc] == -1:
                            break
                        # 1 ~ 5 블럭이면 방향 전환, 득점
                        elif 1 <= B[nr][nc] <= 5:
                            d = change[B[nr][nc]][d]
                            score += 1
                        # 1 ~ 6 블럭이면 같은 번호 웜홀로 이동, 방향 그대로
                        elif 6 <= B[nr][nc] <= 10:
                            nr, nc = wormhole[(nr, nc)]
                        # 한칸 전진
                        nr += dr[d]
                        nc += dc[d]
                    result = max(score, result)

    print("#{} {}".format(tc+1, result))

    # 1 9
    # 2 0
    # 3 7
    # 4 5
    # 5 19