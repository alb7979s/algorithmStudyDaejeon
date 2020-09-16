import sys
sys.stdin = open('4013_input.txt')

from collections import deque

def dfs(num, dir):
    global checked
    checked[num] = 1
    if num > 0:
        if mag[num-1][2] != mag[num][6] and not checked[num-1]:
            dfs(num-1, -dir)
    if num < 3:
        if mag[num][2] != mag[num+1][6] and not checked[num+1]:
            dfs(num+1, -dir)
    if dir == 1:        # 시계
        mag[num].rotate()
    else:               # 반시계
        mag[num].rotate(-1)

# main
T = int(input())
for tc in range(T):
    K = int(input())
    mag = [deque(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        checked = [0] * 4
        n, d = map(int, input().split())
        dfs(n-1, d)

    answer = 0
    for i in range(4):
        answer += mag[i][0] * 2 ** i
    print("#{} {}".format(tc+1, answer))