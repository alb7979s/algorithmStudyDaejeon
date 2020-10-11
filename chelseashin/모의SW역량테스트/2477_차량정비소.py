import sys
sys.stdin = open('2477_input.txt')

# main
T = int(input())
for test_case in range(1, 1 + T):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))

    A, B = A - 1, B - 1     # 지갑 분실한 사람의 이용 창구 번호
    waiting1 = []  # A 대기열
    AA = [None] * N  # A 창구
    AA_num = 0  # A 창구 인원
    waiting2 = []  # B 대기열
    BB = [None] * M  # B 창구
    sub_res = [False] * (K + 1)  # 지갑 떨어뜨린 A 창구에 방문한 손님
    result = 0  # 지갑 분실한 사람과 같은 창구 이용한 사람 수

    time = 0
    idx = 1  # 손님 번호
    while t or AA_num or waiting2:

        # 입장 손님 A 대기열로
        while t and t[0] == time:
            t.pop(0)
            waiting1.append(idx)    # A 대기열에 손님 번호 추가
            idx += 1                # 도착하는 순으로 번호 부여

        # A 대기열 -> A창구 -> B 대기열
        for i in range(N):
            # 창구에 손님 있으면
            if AA[i]:
                AA[i][1] -= 1  # 시간 줄임
                if not AA[i][1]:  # 시간 다 되면
                    waiting2.append(AA[i][0])  # B 대기열로 보내고
                    AA[i] = None  # 창구 비움
                    AA_num -= 1  # 창구 이용 인원 줄임

            # 창구 비면
            if AA[i] is None:
                if waiting1:  # A 대기열 있으면 채움
                    num = waiting1.pop(0)   # 손님 번호
                    AA[i] = [num, a[i]]     # [번호, 남은 시간]
                    AA_num += 1             # A 창구 인원
                    if i == A:  # 지갑 떨어뜨린 A 창구이면
                        sub_res[num] = True

        # B 대기열 -> B 창구 -> 귀가
        for i in range(M):
            # 창구에 손님 있으면
            if BB[i]:
                BB[i][1] -= 1  # 시간 줄임
                if not BB[i][1]:  # 시간 다 되면 창구 비움
                    BB[i] = None

            if BB[i] is None:   # 창구 비면
                if waiting2:  # B 대기열있으면 채움
                    num = waiting2.pop(0)   # 손님 번호
                    BB[i] = [num, b[i]]     # [손님번호, 남은 시간]
                    # 지갑 떨어뜨린 B 창구이면서 A 창구이면 결과 반영
                    if i == B and sub_res[num]:
                        result += num
        time += 1

    # 손님 없으면
    if not result:
        result = -1

    print('#{} {}'.format(test_case, result))
    # 1 3
    # 2 7
    # 3 2
    # 4 22
    # 5 18
    # 6 15
    # 7 -1
    # 8 259
    # 9 100
    # 10 164