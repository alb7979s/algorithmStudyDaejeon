import sys
sys.stdin = open("1406_input.txt")

# 스택 2개로 Solve
alpha = input()
left = list(alpha)
right = []
M = int(input())

print(left, right)
for _ in range(M):
    temp = list(map(str, input().split()))
    if temp[0] == "L":  # 커서 왼쪽으로 한 칸 이동
        if left:
            right.append(left.pop())
    elif temp[0] == "D":    # 커서 오른쪽으로 한 칸 이동
        if right:
            left.append(right.pop())
    elif temp[0] == "P":    # 커서 왼쪽에 문자 추가
        left.append(temp[1])
    elif temp[0] == "B":    # 커서 왼쪽 문자 삭제
        if left:
            left.pop()
    print(left, right)

print(''.join(left + right[::-1]))