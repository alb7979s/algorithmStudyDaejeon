import sys
sys.stdin = open('5658_input.txt')

from collections import deque

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    S = deque(input())
    n = N//4

    numbers = set()
    # 회전한 상태
    for _ in range(N//4):
        for i in range(0, N, n):
            temp = ''
            for j in range(n):
                temp += S[i+j]
            numbers.add(int(temp, 16))
        S.rotate()

    print("#{} {}".format(tc+1, sorted(numbers)[::-1][K-1]))

# 다른 풀이
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     data = input() * 2
#     ans = set()
#     for i in range(N // 4):
#         for j in range(1, 5):
#             ans.add(int(data[i + (N // 4) * (j - 1) : i + (N // 4) * j], 16))
#     print("#{} {}".format(test_case + 1, sorted(ans)[:: - 1][K - 1]))