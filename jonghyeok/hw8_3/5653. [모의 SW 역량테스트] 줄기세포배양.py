#1. X시간동안 비활성
#2. X시간 지나는 순간 활성 => 활성 되는 순간 4방향 번식(이미 있음 번식x, 동시=> 생명력 높은 아이로)
#3. X시간 후 죽음

#2번 할람 activeList 따로 처리 해주고 visit도 이 때 처리해줘야할듯
#1번 살아있는 세포들 생명력은 heapq로 처리해줄수 있을듯 (현재생명력, 활성상태, x, y, 생명력크기)
from heapq import*
for tc in range(int(input())):
    n, m, k = map(int,input().split())  #열, 행, k초
    aliveList=[]
    visit={}
    for i in range(n):
        a=list(map(int,input().split()))
        for j in range(m):
            if a[j]:
                heappush(aliveList, (a[j], 0, i, j, a[j]))
                visit[i, j] = 1
    for t in range(1, k+1):
        activeList={}
        #생명력 비교
        while aliveList:
            cur, f, x, y, life = heappop(aliveList)
            if cur > t:
                heappush(aliveList, (cur, f, x, y, life))
                break
            else:
                if not f:   #비활성이면 활성으로
                    heappush(aliveList, (life+t, 1, x, y, life))
                    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        nx, ny = x+dx, y+dy
                        if (nx, ny) in visit: continue
                        if (nx, ny) in activeList:
                            activeList[nx, ny] = max(activeList[nx, ny], life)
                        else:
                            activeList[nx, ny] = life
        # print(len(aliveList))
        # print(len(activeList))
        if t==k: continue           #마지막 추가 해주는거 때문에 틀린답 나왔었음
        for [x, y], life in activeList.items():
            visit[x, y] = 1
            heappush(aliveList, (t+life+1, 0, x, y, life))
    print('#{} {}'.format(tc+1, len(aliveList)))

