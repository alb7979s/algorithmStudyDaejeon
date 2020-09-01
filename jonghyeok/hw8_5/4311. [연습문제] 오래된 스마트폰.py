from collections import*
# from itertools import permutations 이 모듈 못씀 -_;
INF=int(1e9)
#모듈 못써서 직접 구현, 중복 가능한 순열
class Permutations:
    def __init__(self, arr):
        self.res=[]
        self.st=[]
        self.visit=[False]*len(arr)
    def permutations(self, arr, limit):
        self._permutations(arr, 0, limit)
        return self.res
    def _permutations(self, arr, cnt, limit):
        if cnt == limit:
            temp = []
            for x in self.st:
                temp.append(x)
            #st 통째로 넣으면 오류남
            self.res.append(temp)
            return
        for i in range(len(arr)):
            self.st.append(arr[i])
            self._permutations(arr, cnt+1, limit)
            self.st.pop()
#+-*/
def cal(a, b, c):
    if b==1: return a+c
    if b==2: return a-c
    if b==3: return a*c
    if b==4 and c: return a//c
    return INF
#main
for tc in range(int(input())):
    n, o, m = map(int,input().split())
    activeNum = list(map(int,input().split()))
    activeOp = list(map(int,input().split()))
    w = int(input())
    numSet = set()
    #0~999 (1자리~3자리 까지 올 수 있음) 까지 주어진 숫자들로 만들 수 있는 조합들 다 구함
    for i in range(1, 4):
        per = Permutations(activeNum)
        for p in per.permutations(activeNum, i):
            temp=''
            for x in p:
                temp+=str(x)
            numSet.add(int(temp))
    q=deque()   #(누른 횟수, 현재 값, flag)
    visit=[0]*1000
    for x in numSet:
        lx = len(str(x))    #문자열로 바꾼 길이가 누른 횟수(다 한자릿수의 숫자니까)
        q.append((lx, x, 0))
        visit[x] = lx       #visit = 몇번만에 눌러서 그 값에 도착했는지 나타내는 배열
    # print(numSet)
    res = INF
    while q:
        cnt, x, f = q.popleft()     #f처음에 0이고 연산 사용하면 1로 바뀜
        if x == w:                  #답이면 갱신
            res = min(res, cnt + f)
        for y in numSet:
            nc = cnt + visit[y] + 1 #여기까지 누른 수 + 다음 누를 숫자 누르는데에 드는 수 + 연산자 누르는거 1까지
            if nc+f > m: continue   #다음 버튼이 m 넘으면 끝냄
            for op in activeOp:     #가능한 연산자들로 계산
                nx = cal(x, op, y)
                if 0 <= nx <= 999:
                    if not visit[nx] or visit[nx] > nc: #visit 초기값이거나 nc(다음숫자까지 누른 횟수)가 더 작으면 갱신
                        visit[nx] = nc
                        q.append((nc, nx, 1))
    print('#%d %d'%(tc+1, res if res != INF else -1))
