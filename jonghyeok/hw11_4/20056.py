from sys import*
input=stdin.readline
from collections import*

dd = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] #위부터 시계방향
n,M,K=map(int,input().split())
q=deque()
for i in range(M):
    x, y, m, s, d = map(int,input().split())            #속력은 건드리면 안됨, 나중에 합을 나누는 연산에 쓰임
    q.append((x-1, y-1, m, s, d))
for i in range(K):
    visit = {}
    while q:
        x, y, m, s, d = q.popleft()
        dx, dy = dd[d]
        #음수 나머지 연산 신경쓰이니 n*250해서 양수로 바꿔줌
        x, y = (n*250+x+dx*s)%n, (n*250+y+dy*s)%n       #음수로 갈 수 있으니 n만큼 더해서 속력만큼 가고 n나머지
        if (x, y) not in visit:
            visit[(x, y)] = [m, s, d, 1]                #질량, 속력, 방향 홀/짝, 개수
        else:
            visit[(x, y)][0] += m
            visit[(x, y)][1] += s
            if visit[(x, y)][2]%2 != d%2: visit[(x, y)][2] = 8        #다른 경우만 8로 처리
            visit[(x, y)][3] += 1
    for k, v in visit.items():
        x, y = k
        m, s, d, cnt = v
        #두개이상 합쳐진 곳이면 4등분
        if cnt >= 2:
            m = int(m/5)
            if m == 0: continue
            s = int(s/cnt)
            if d!=8:    #0, 2, 4, 6
                for d in [0, 2, 4, 6]:
                    q.append((x, y, m, s, d))
            else:       #1, 3, 5, 7
                for d in [1, 3, 5, 7]:
                    q.append((x, y, m, s, d))
        else:
            q.append((x, y, m, s, d))
res = 0
while q:
    x, y, m, s, d = q.popleft()
    res += m
print(res)
