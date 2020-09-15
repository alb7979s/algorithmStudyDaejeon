import sys
sys.stdin = open('4014_input.txt')

# 카운트는 경사로의 길이와 비교하기 위해 필요
# 길의 높이가 같다면, 카운트 1 증가. 
# 올라가는 경사로라면, 카운트가 경사로의 길이 X 이상인지 확인. 카운트가 X 이상이면, 경사로를 놓을 수 있는 경우이므로, 카운트 1로 초기화.
# 내려가는 경사로라면, 카운트가 0 이상인지 확인. 0 이상이라면, 카운트를 경사로의 길이 X 만큼 음수로 만듦.
# 만약 카운트가 음수라면, 내려가는 경사로를 만들고 있는 중이므로, 경사로를 놓을 수 없다.

def check_slope(L):
    global ans
    cnt = 1
    for i in range(1, N):
        if L[i] == L[i-1]:
            cnt += 1
        elif L[i] - L[i-1] == 1 and cnt >= X:   # 땅의 높이가 이전보다 높으면
            cnt = 1
        elif L[i-1] - L[i] == 1 and cnt >= 0:    # 땅의 높이가 이전보다 낮으면
            cnt = -X+1
        else:
            break
    else:
        if cnt >= 0:
            ans += 1

# main
T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = list(map(list, zip(*A)))    # 세로 검사
    ans = 0
    for n in range(N):
        check_slope(A[n])
        check_slope(B[n])

    print("#{} {}".format(tc+1, ans))