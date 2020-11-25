from collections import*
n,m=map(int,input().split())
q=deque()
res = '<'
for i in range(1, n+1):
    q.append(i)
for i in range(n):
    for j in range(m-1):
        q.append(q.popleft())
    res += str(q.popleft())+', '
print(res[:-2]+'>')
