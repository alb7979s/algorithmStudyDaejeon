import sys
sys.stdin = open('15685_input.txt')

# 다음에 풀 땐 큐로 풀어보자!

# 우, 상, 좌, 하
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)

N = int(input())
A = [[0] * 101 for _ in range(101)]

for _ in range(N):
    c, r, d, g = map(int, input().split())
    curve = [d]
    for i in range(g):
        C = len(curve)
        for j in range(C-1, -1, -1):        # 역순으로 세대마다 추가한
            curve.append((curve[j]+1) % 4)  # 방향 반대로 바꾸면서 추가
    A[r][c] = 1
    
    # 방향들을 담은 리스트 돌리면서 배열에 그려줌
    for dir in curve:
        r += dr[dir]
        c += dc[dir]
        A[r][c] = 1

# 배열에 모두 다 그리면 한번에 정사각형 네 점의 존재유무 확인
square = 0
for i in range(100):
    for j in range(100):
        if A[i][j] and A[i][j+1] and A[i+1][j] and A[i+1][j+1]:
            square += 1
print(square)