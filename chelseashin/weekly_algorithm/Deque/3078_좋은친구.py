import sys
sys.stdin = open("3078_input.txt")
input = sys.stdin.readline

# 시간초과..
# def comb(depth, k):
#     global pair
#     if depth == 2:
#         print(order)
#         if friends[order[0]] == friends[order[1]]:
#             pair += 1
#         return
#     for i in range(K):
#
#         order.append(k+i)
#         comb(depth+1, i+1)
#         order.pop()
#
# N, K = map(int, input().split())
# friends = [len(input().strip()) for _ in range(N)]
# # print(friends)
#
# pair = 0
# order = []
# comb(0, 0)
# print(pair)

# DP로 접근 - 아무리 생각해도 무슨 원리인지 모르겠다,,
N, K = map(int, input().split())
students = [0] * N
dp = [0] * 21
cnt = 0
for rank in range(N):
    length = len(input().strip())
    students[rank] = length
    if rank > K:
        dp[students[rank-K-1]] -= 1
    cnt += dp[length]
    dp[length] += 1
    # print("rank", rank, students)
    # print("dp", dp)
    # print("cnt", cnt)
    # print()
print(cnt)