import sys
sys.stdin = open('2382_input.txt')

# 맵 없이도 충분히 풀 수 있는 문제!
# 약품(테두리) 닿으면 방향 전환, 개체 수 반감
# 딕셔너리 활용하여 이동 위치가 중복될 때 흡수 시킬지 흡수 당할지를 결정


# 상 하 좌 우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

# 방향 바꾸기
rev = (0, 2, 1, 4, 3)

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(K)]

    # M 시간 동안 미생물 군집 격리
    for _ in range(M):
        check = dict()
        idx = -1
        for info in raw:
            r, c, cnt, d = info
            idx += 1
            if not cnt:
                continue

            # 이동
            nr = r + dr[d]
            nc = c + dc[d]
            info[0], info[1] = nr, nc
            # 약품에 닿으면 개체 수 반감, 방향 전환
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                info[2] //= 2
                info[3] = rev[info[3]]
            # 중복체크
            if (nr, nc) not in check:           # 좌표에 아무도 없으면
                check[(nr, nc)] = (idx, cnt)    # 최대 미생물 등록
            else:   # 좌표에 이미 있으면
                max_idx, max_cnt = check[(nr, nc)]  # 최대 미생물
                if max_cnt < cnt:
                    check[(nr, nc)] = (idx, cnt)    # 등록
                    info[2] += raw[max_idx][2]      # 흡수
                    raw[max_idx][2] = 0
                else:   # 작으면
                    raw[max_idx][2] += info[2]      # 흡수 당함
                    info[2] = 0

    # 남은 미생물 수
    microbe = 0
    for R in raw:
        microbe += R[2]

    print("#{} {}".format(tc+1, microbe))