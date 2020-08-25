#한 칸 회전하는 함수
#n//4씩 잘라서 set()에 저장
#총 (n//4)-1 동안 회전
def rotate():
    global a
    #시계든 반시계든 모든 가지수 구할람 똑같음
    for i in range(N-1):
        a[i], a[i+1] = a[i+1], a[i]
def solve():
    global a
    side = N//4
    for i in range(side):           #총 회전수
        for j in range(4):          #4방향 탐색
            temp=''
            for k in range(side):   #한 방향씩 처리
                temp+=a[(j*side)+k]
            res.add(int(temp, 16))
        rotate()
    return sorted(list(res),reverse=True)[K-1]
for tc in range(int(input())):
    N, K = map(int,input().split())
    a=list(input())
    res=set()
    print('#{} {}'.format(tc+1, solve()))
