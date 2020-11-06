from collections import*
n=int(input())
a=list(map(int,input().split()))
q=deque()
for i in range(n):
    q.append((a[i],i+1))
while 1:
    x, idx = q.popleft()
    print(idx, end=' ')
    if not q: break
    if x<0:
        for i in range(abs(x)):
            q.appendleft(q.pop())
    else:
        for i in range(x-1):
            q.append(q.popleft())
