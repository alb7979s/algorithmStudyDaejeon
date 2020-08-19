import sys
sys.stdin = open('13458_input.txt')

N = int(input())    # 시험장 수
A = list(map(int, input().split()))   # 응시자 수
B, C = map(int, input().split())
# print(N, A, B, C)

ans = 0
for students in A:
    # 주 감독관
    ans += 1
    students -= B
    if students < 0:
        students = 0
    # 부 감독관
    if students % C == 0:
        ans += students // C
    else:
        if students < C:
            ans += 1
        else:
            ans += students // C + 1

print(ans)