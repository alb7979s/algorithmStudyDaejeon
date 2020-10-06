INF=1e9+1
def cal(x, op, y):
    if op==0: return x+y
    if op==1: return x-y
    if op==2: return x*y
    if op==3: return int(x/y)
def solve(pos, sum):
    global MAX, MIN
    if pos == n:
        MAX = max(MAX, sum)
        MIN = min(MIN, sum)
        return
    for i in range(4):
        if operator[i]:
            operator[i]-=1
            solve(pos+1, cal(sum, i, a[pos]))
            operator[i]+=1
for tc in range(int(input())):
    n=int(input())
    #+-*/
    operator = list(map(int,input().split()))
    a=list(map(int,input().split()))
    MAX, MIN = -INF, INF
    solve(1, a[0])
    print('#{} {}'.format(tc+1, MAX-MIN))
