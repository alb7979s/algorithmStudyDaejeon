from sys import*
from collections import*
input=lambda:stdin.readline().strip()
n, k = map(int,input().split())
q=deque(['?'for _ in range(n)])
#알파벳 한번씩만 사용가능...
alp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
visit={}
for i in range(k):
    inp=list(map(str,input().split()))
    for j in range(int(inp[0])):
        q.appendleft(q.pop())
    if q[0]==inp[1] or (q[0]=='?' and inp[1] not in visit):
        q[0] = inp[1]
        visit[inp[1]]=1
    else:
        print('!')
        exit()
while q:
    print(q.popleft(),end='')
        
    
