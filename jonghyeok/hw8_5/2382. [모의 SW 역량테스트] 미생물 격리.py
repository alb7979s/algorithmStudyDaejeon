from collections import*
#import sys
#sys.stdin = open('test.txt')

#N*N, 가장자리 약품
#위치, 미생물 수, 이동방향
#1시간마다 이동방향에 있는 다음 셀로
#약품 => 미생물 절반으로(소수점 버림), 방향 반대로, 미생물 0이면 사라짐
#이동 후에 두 개 이상의 군집 모이면 합침, 이동 방향은 큰아이 방향
#M시간 후 남아있는 미생물의 총합은?
#상하좌우(1,2,3,4)

#브레인스토밍
'''
큐에 넣고 m시간 동안 큐 길이만큼씩 돌려가지고 미생물 움직임
visit[x][y] = [미생물, 방향, 가장 큰 미생물] 해서 마지막에 처리, dict() 이용하면 편할듯
가장 자리 닿으면 미생물 반 처리, 이동 반대로  
'''
def changeD(d):
    if d==0: return 1
    if d==1: return 0
    if d==2: return 3
    if d==3: return 2
dd = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상 하 좌 우
for tc in range(int(input())):
    n, m, k = map(int,input().split())  #n*n, m시간
    q=deque()
    for i in range(k):
        x, y, z, d = map(int,input().split())
        q.append((x, y, z, d-1))
    for i in range(m):
        visit={}
        lq = len(q)
        for i in range(lq):
            x, y, z, d = q.popleft()
            dx, dy = dd[d]
            nx, ny = x+dx, y+dy
            if nx==0 or ny==0 or nx==n-1 or ny==n-1:
                #모서리에서 겹칠 일 없음
                q.append((nx, ny, z//2, changeD(d)))
            else:
                if (nx, ny) in visit:   #있으면 합치고, 가장 큰 친구 비교
                    visit[nx, ny][0] += z
                    if visit[nx, ny][2] < z:
                        visit[nx, ny][1] = d
                        visit[nx, ny][2] = z
                else:
                    visit[nx, ny] = [z, d, z]
        for [x, y], [z, d, z2] in visit.items():
            q.append((x, y, z, d))
    res = 0
    while q:
        x, y, z, d = q.popleft()
        res += z
    print('#{} {}'.format(tc+1, res))

