import sys
sys.stdin = open("1725_input.txt")
input = sys.stdin.readline
N = int(input())
L = [int(input()) for _ in range(N)] + [0]
# print(N, L)

# O(N^2) 풀이 - 당연히 실패! 시간초과..
# MAX = float('-inf')
# for i in range(1, N+1):
#     for j in range(N-i+1):
#         # print(i, j, L[j:j+i], i * min(L[j:j+i]))
#         MAX = max(MAX, i*min(L[j:j+i]))
# print(MAX)

# O(N) 풀이 - 스택으로 풀기!
# 참고 - https://private-space.tistory.com/12
# cursor : 현재 x좌표 값(이후 (i-cursor)을 이용해서 가로길이 구함)
# stack : 튜플(x좌표 값, 높이)를 저장하는 스택
ans = 0
cursor = 0
stack = [(0, L[0])]
# print(stack, ans)
for i in range(1, N+1):
    # print("상태", i, "일 때")
    cursor = i
    while stack and stack[-1][1] > L[i]:
        cursor, temp = stack.pop()
        ans = max(ans, temp * (i-cursor))
        # print(i, (cursor, L[i]), stack, temp * (i-cursor))
    stack.append((cursor, L[i]))
    # print('스택', stack)
    # print()
    
print(ans)

# 스택에 들어있는 막대보다 다음의 막대가 크거나 같으면 그냥 스택에 넣고,
# 그게 아니라면
# 현재 들어있는 막대 중 다음에 넣을 막대보다 큰 막대들을 전부 빼내며 넓이를 계산한 후
# 스택에 넣는 것이다.