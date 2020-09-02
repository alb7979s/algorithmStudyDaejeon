#import sys
#sys.stdin = open('C:/projects/mysite/algorithms/test.txt')
from collections import*
#D*W 보호필름
#특성 A or B
#합격기준 k
#세로 방향으로 동일 특성 셀 k개 이상만 성능 검사 통과
#약품 사용 => 행마다 투입 가능, 그 행 A or B의 셀로 바꿈
#약품 최소로 사용하는 횟수는?
#완탐(각 행마다 약품사용x, A, B) 3**13 = 약 160만 가능

#일단 풀고 최적화
#BFS() 가능?
#약품 했을때 배열 바꾸지 말고 그냥 그 부분들만 논리적으로 처리 가능?

'''
모든 행의 경우를 A or B로 바꿔가며 확인하다가 찾으면 return
연속 된거 찾아주는 함수 만들고
'''
INF=int(1e9)
def check():
    for i in range(m):
        maxCnt = 1
        cnt = 1
        for j in range(n-1):
            if a[j][i] == a[j+1][i]:
                cnt+=1
            else:
                cnt=1
            maxCnt = max(maxCnt, cnt)
        if maxCnt < k:
            return 0
    return 1
def solve(pos, cnt):
    global a, res
    if cnt > k or res <= cnt: return res
    if pos == n:
        if check():
            res = min(res, cnt)
        return res
    res = min(res, solve(pos+1, cnt))
    temp=[]
    #A약품 처리
    for i in range(m):
        temp.append(a[pos][i])  #되돌릴 값 저장해놓음
        a[pos][i] = 0
    res = min(res, solve(pos+1, cnt+1))
    #B약품 처리
    for i in range(m):
        a[pos][i] = 1
    res = min(res, solve(pos+1, cnt+1))
    #되돌리기
    for i in range(m):
        a[pos][i] = temp[i]
    return res

for tc in range(int(input())):
    n, m, k = map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    res=INF
    print('#{} {}'.format(tc+1, solve(0, 0)))
