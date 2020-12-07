N, K = 7, 3

# 나의 풀이 - 메모리, 시간 모두 더 효율적
N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]
answer = "<"
idx = 0
while len(circle):
    if idx >= 0:
        idx = (idx + K) % len(circle)
        idx -= 1
    else:
        idx = (idx + K) % len(circle)
    answer += str(circle.pop(idx)) + ", "

print(answer[:-2] + ">")

# 다른 풀이 - deque 사용
#
# from collections import deque
# Q = deque([i for i in range(1, N+1)])
# res = '<'
# for i in range(N):
#     for _ in range(K-1):
#         Q.append(Q.popleft())
#     res += str(Q.popleft()) + ", "
# print(res[:-2] + ">")