import sys
sys.stdin = open('19238_input.txt')
input = sys.stdin.readline
from collections import deque
from heapq import heappush

# 상 좌 우 하
dr = (-1, 0, 0, 1)
dc = (0, -1, 1, 0)

def move(sr, sc):
    visited = [[-1] * N for _ in range(N)]
    Q1 = deque([(sr, sc)])
    visited[sr][sc] = 0
    while Q1:
        r, c = Q1.popleft()
        if (r, c) == info[(sr, sc)]:
            return [visited[r][c], r, c]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc] == 1:
                continue
            if visited[nr][nc] >= 0:
                continue
            visited[nr][nc] = visited[r][c] + 1
            Q1.append((nr, nc))
    return [-1, 0, 0]

def bfs(sr, sc):
    if A[sr][sc] == 2:
        return [0, sr, sc]
    visited = [[-1] * N for _ in range(N)]
    Q = deque([(sr, sc)])
    visited[sr][sc] = 0
    priority = []
    while Q:
        if not Q:
            break
        qlen = len(Q)
        for _ in range(qlen):
            flag = 0
            r, c = Q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if A[nr][nc] == 1:
                    continue
                if visited[nr][nc] >= 0:
                    continue
                if A[nr][nc] == 2:  # 타겟 찾으면
                    flag = 1
                    visited[nr][nc] = visited[r][c] + 1
                    heappush(priority, (visited[nr][nc], nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
            if flag:
                break
    if priority:
        return priority[0]
    return [-1, 0, 0]

# main
N, M, fuel = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
br, bc = map(int, input().split())
br -= 1
bc -= 1
info = dict()
for _ in range(M):
    sr, sc, gr, gc = map(int, input().split())
    info[(sr-1, sc-1)] = (gr-1, gc-1)
    A[sr-1][sc-1] = 2
cnt = 0

while fuel:
    if cnt == M:
        print(fuel)
        break
    # 1. 태울 승객 탐색
    temp = bfs(br, bc)
    if temp[0] != -1:
        start = temp
    else:
        print(-1)
        break

    if fuel - start[0] >= 0:
        fuel -= start[0]    # 승객 태우러 가기까지 연료 소모
    else:   # 연료 없으면 영업 종료
        print(-1)
        break
    # 2. 승객 태우고 이동
    d, r, c = start
    destination = move(r, c)
    # 목적지에 도달하면
    if destination[0] != -1:
        if fuel - destination[0] >= 0:
            fuel -= destination[0]    # 승객 목적지까지 연료 소모
            fuel += destination[0] * 2
            # 승객 이동 완료되면 정보 지우기
            br, bc = destination[1], destination[2]  # 택시 현재 위치 갱신
            A[r][c] = 0
            del info[(r, c)]
            cnt += 1  # 승객 한명 완료
        else:   # 연료 없으면 영업 종료
            print(-1)
            break
    # 목적지에 도달하지 못하면
    else:
        print(-1)
        break