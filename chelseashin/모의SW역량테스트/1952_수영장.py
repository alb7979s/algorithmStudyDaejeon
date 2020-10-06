import sys
sys.stdin = open('1952_input.txt')

def backtracking(pos, pay):
    global MIN
    if pos >= 12:
        MIN = min(MIN, pay)
        return
    if plan[pos] == 0:  # 현재 달에 이용일이 없을 경우 다음 달로 넘어감
        backtracking(pos+1, pay)
    else:   # 현재 달에 이용일이 있는 경우 3가지 선택지
        backtracking(pos+1, pay + plan[pos] * day)
        backtracking(pos+1, pay + month)
        backtracking(pos+3, pay + quarter)

T = int(input())
for tc in range(T):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))

    MIN = year  # 최솟값 1년 이용권 금액으로 설정
    backtracking(0, 0)
    print("#{} {}".format(tc+1, MIN))

    # 1 110
    # 2 100
    # 3 400
    # 4 530
    # 5 430
    # 6 1080
    # 7 1840
    # 8 800
    # 9 1980
    # 10 2260