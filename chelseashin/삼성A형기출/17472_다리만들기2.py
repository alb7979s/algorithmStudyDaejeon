import sys
sys.stdin = open('17472_input.txt')

# MST 최소신장트리 공부해보기
# https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html

# 제한
# 1 ≤ N, M ≤ 10
# 3 ≤ N×M ≤ 100
# 2 ≤ 섬의 개수 ≤ 6

from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 섬 라벨링
def bfs(r, c, isl_num):
    Q.append([r, c])
    isl_num_map[r][c] = isl_num
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and isl_num_map[nr][nc] == -1:
                if sea[nr][nc]:
                    isl_num_map[nr][nc] = isl_num
                    Q.append([nr, nc])

# 시작좌표(sr, sc), 4방향 중 하나(dir, 항상 다리는 한 방향),
# 다리 길이(bridge_dis), 현재 값(start, 시작 섬의 번호)
def dfs(r, c, dir, bridge_dis, start):
    nr = r + dr[dir]
    nc = c + dc[dir]
    if not 0 <= nr < N or not 0 <= nc < M:
        return
    if sea[nr][nc] == 1:
        end = isl_num_map[nr][nc]   # 도착 섬의 번호
        if start == end:            # 자기 자신 섬이면 return
            return
        if bridge_dis == 1:         # 다리 길이 1이면 return
            return
        else:
            # 시작 섬과 끝 섬 사이의 최소 거리 갱신
            isl_min_dis[start][end] = min(bridge_dis, isl_min_dis[start][end])
            return
    bridge_dis += 1
    dfs(nr, nc, dir, bridge_dis, start)


def find_min(cnt, index, end):
    global min_ans
    if cnt == end:
        # print(select)
        Q = deque()
        V = [0 for _ in range(isl_num)]
        isl_cnt = 1              # 연결할 수 있는 섬의 갯수 세기
        bridge_length = 0        # 총 다리 길이
        for i in range(isl_num):
            if not V[i]:
                Q.append(i)
                V[i] = 1
                while Q:
                    sx = Q.popleft()
                    for nx in i2i[sx]:
                        if select[i2i_bridge[sx][nx]] and not V[nx]:
                            V[nx] = 1
                            Q.append(nx)
                            isl_cnt += 1
                            bridge_length += isl_min_dis[sx][nx]

        if isl_cnt == isl_num:
            min_ans = min(min_ans, bridge_length)
            # print('isl_cnt', isl_cnt, bridge_length)
        return

    for i in range(index, bridge_num):
        select[i] = 1
        find_min(cnt+1, i+1, end)
        select[i] = 0

# main
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
isl_num_map = [[-1]*M for _ in range(N)]

# 1. bfs로 각 섬의 번호 라벨링
#    isl_num : 섬에 붙일 번호이자 섬의 갯수
#    isl_num_map : 각 섬에 번호가 붙여진 배열
isl_num = 0
Q = deque()
for i in range(N):
    for j in range(M):
        if sea[i][j] and isl_num_map[i][j] == -1:
            bfs(i, j, isl_num)
            isl_num += 1
# print('isl_num_map', isl_num_map)

# 2. dfs로 입력한 방향으로 계속 이동하면서 다른 섬을 만나는지 확인
#    같은 섬을 만난 경우와 길이가 1인 경우는 예외로 처리
#    isl_min_dis: 두 섬사이의 최소 다리 길이를 저장한 배열
isl_min_dis = [[10]*isl_num for _ in range(isl_num)]
for i in range(N):
    for j in range(M):
        if sea[i][j]:
            for k in range(4):
                dfs(i, j, k, 0, isl_num_map[i][j])
# print('isl_min_dis', isl_min_dis)

# 3. 두 섬을 연결하는 다리에 번호를 붙이고 섬을 서로 연결한 배열을 만든다
#    i2i_bridge : 두 섬을 연결한 다리의 번호를 저장한 배열
#    i2i : 현재 위치에서 어느 섬으로 이동할 수 있는지 저장한 배열
#    bridge_num : 각 다리에 붙일 번호이자 다리의 개수
i2i_bridge = [[-1]*isl_num for _ in range(isl_num)]
i2i = [[] for _ in range(isl_num)]      # 인접행렬
bridge_num = 0
for i in range(isl_num-1):
    for j in range(i+1, isl_num):
        if isl_min_dis[i][j] < 10:
            i2i_bridge[i][j] = bridge_num
            i2i_bridge[j][i] = bridge_num
            i2i[i].append(j)
            i2i[j].append(i)
            bridge_num += 1

# print('i2i_bridge', i2i_bridge)
# print('i2i', i2i)
# print('bridge_num', bridge_num)

# 4. find_min 함수에서 dfs로 다리를 고르고 bfs로 모든 섬을 이동할 수 있는지 확인
#    select : dfs로 어떤 다리 선택했는지 저장하는 배열
#    start : 다리를 몇 개부터 선택할지 정하는 변수
#    isl_cnt : bfs로 이동하면서 몇 개의 섬을 지났는지 저장하는 변수
#    bridge_length : 다리의 총 길이를 더하는 변수
#    min_ans : 최소 다리의 길이를 저장하는 변수(다리)
select = [0 for _ in range(bridge_num)]
if isl_num % 2 == 0:
    start = isl_num // 2
else:
    start = (isl_num // 2) + 1
min_ans = float('inf')
for i in range(start, bridge_num+1):
    find_min(0, 0, i)   # dfs로 다리 고르기(i는 고를 갯수)

if min_ans == float('inf'):
    print(-1)
else:
    print(min_ans)