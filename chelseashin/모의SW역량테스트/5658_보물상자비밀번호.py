import sys
sys.stdin = open('5658_input.txt')

from collections import deque

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    S = deque(input())
    n = N//4
    
    # 처음 상태
    numbers = set()
    for i in range(0, N, n):
        temp = ''
        for j in range(n):
            temp += S[i+j]
        numbers.add(int(temp, 16))
    # 회전한 상태
    for _ in range(N//4):
        S.rotate()
        for i in range(0, N, n):
            temp = ''
            for j in range(n):
                temp += S[i+j]
            numbers.add(int(temp, 16))

    print("#{} {}".format(tc+1, sorted(numbers)[::-1][K-1]))