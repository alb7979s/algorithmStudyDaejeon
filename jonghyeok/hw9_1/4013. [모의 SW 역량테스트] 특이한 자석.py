#import sys
#sys.stdin = open('C:/projects/mysite/algorithms/test.txt')
def turn(x, d):
    visit[x]= d
    if x-1 >= 0 and not visit[x-1] and a[x-1][2] != a[x][-2]:
        turn(x-1, -d)
    if x+1 < 4 and not visit[x+1] and a[x][2] != a[x+1][-2]:
        turn(x+1, -d)
def rotate():
    for i in range(4):
        if visit[i]:
            temp = []
            for j in range(8):
                temp.append(a[i][j])
            for j in range(8):
                if visit[i]==1:
                    a[i][j] = temp[(j+7)%8] #시계
                else:
                    a[i][j] = temp[(j+1)%8] #반시계
for tc in range(int(input())):
    k = int(input())
    a = [list(map(int,input().split())) for _ in range(4)]
    for i in range(k):
        visit=[0]*4
        x, d = map(int,input().split())
        turn(x-1, d)
        rotate()
    res=0
    for i in range(4):
        if a[i][0]: res += (1<<i)
    print("#{} {}".format(tc+1, res))
