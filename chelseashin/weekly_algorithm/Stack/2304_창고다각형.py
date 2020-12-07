import sys
sys.stdin = open("2304_input.txt")
input = sys.stdin.readline

min_L = float('inf')
max_L = 1
max_H_idx = 0
max_H_val = 0

N = int(input())
heights = []
for _ in range(N):
    L, H = map(int, input().split())
    heights.append((L, H))
    if L < min_L:   # 가장 왼쪽 위치
        min_L = L
    if L > max_L:   # 가장 오른쪽 위치
        max_L = L
    # 최고 높이일 때의 인덱스와 값
    if H > max_H_val:
        max_H_val = H
        max_H_idx = L

# 기둥 높이 리스트
temp = [0] * (max_L + 1)
for l, h in heights:
    temp[l] = h

# 왼쪽부터 top까지 탐색
left = 0
answer = 0
for i in range(max_H_idx+1):
    if temp[i] > left:
        left = temp[i]
    answer += left
# 오른쪽부터 top까지 탐색
right = 0
for j in range(max_L, max_H_idx, -1):
    if temp[j] > right:
        right = temp[j]
    answer += right

print(answer)