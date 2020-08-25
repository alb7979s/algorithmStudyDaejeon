import sys
sys.stdin = open('5656_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def down(depth):
    remain = []
    for c in range(W):
        for r in range(H):
            if raw_data[depth][r][c]:
                remain.append(raw_data[depth][r][c])
        remain = [0] * (H - len(remain)) + remain
        for r in range(H-1, -1, -1):
            raw_data[depth][r][c] = remain.pop()

# 벽돌 깨기
def boom(depth, sr, sc):
    boom_count = 0
    # 현재 depth에 작업하기 전에 전 depth의 결과를 복사해온다.
    raw_data[depth+1] = [R[:] for R in raw_data[depth]]
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        power = raw_data[depth+1][r][c]
        if power == 0:
            continue
        raw_data[depth+1][r][c] = 0
        boom_count += 1

        for i in range(4):
            for j in range(1, power):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if not raw_data[depth+1][nr][nc]:
                    continue
                stack.append((nr, nc))
    down(depth+1)
    return boom_count

# 구슬 쏜 횟수, 깬 벽돌 수
def dfs(depth, count):
    global total
    if total == brick:
        return
    # 구슬 N번 모두 쏘거나, 벽돌 다 깼을 경우
    if depth == N or count == brick:
        total = max(total, count)
        return
    for w in range(W):
        for h in range(H):
            if raw_data[depth][h][w]:
                dfs(depth+1, count + boom(depth, h, w))
                break

# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    raw_data = [[[0] * W for _ in range(H)] for _ in range(N+1)]
    brick = 0
    for i in range(H):
        raw_data[0][i] = list(map(int, input().split()))
        brick += sum(1 for j in raw_data[0][i] if j)
    total = 0
    dfs(0, 0)
    print("#{} {}".format(tc+1, brick-total))