from sys import*
from collections import*
input=stdin.readline
for tc in range(int(input())):
    n,m,k,A,B = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    t=list(map(int,input().split()))
    end, cnt = 0, 0
    reception = [0]*n
    repair = [0]*m
    repairWait = deque()
    idx, time = 0, 0
    while 1:
        if end == k: break
        #접수 들어오는거 처리
        for i in range(n):
            if idx >= k or t[idx]>time: break
            if not reception[i]:
                reception[i] = (time+a[i]-1, idx+1, i)   #끝나는 시각, 고객번호, 몇번째 창구인지
                idx+=1
        # print(time, reception)
        #수리 들어오는거 처리
        for i in range(m):
            if not repairWait:break
            if not repair[i]:
                t1, t2 = repairWait.popleft()
                repair[i] = (time+b[i]-1, t1, t2, i)  #끝나는 시각, 고객번호, 접수창구, 수리창구
        #접수 끝나는거 처리
        for i in range(n):
            if reception[i] and reception[i][0] <= time:
                repairWait.append((reception[i][1], reception[i][2]))
                reception[i] = 0
        #수리 끝나는거 처리
        # print(time, repair)
        for i in range(m):
            if repair[i] and repair[i][0] <= time:
                end += 1
                t1, t2, t3, t4 = repair[i]
                if t3 == A-1 and t4 == B-1: cnt+=t2
                repair[i] = 0
        time+=1
    print('#{} {}'.format(tc+1, cnt if cnt else -1))
