from collections import*
n,m=map(int,input().split())
q=deque()
for i in range(1, n+1):
    q.append(i)
pick = list(map(int,input().split()))
cnt = 0
for i in range(m):
    leftRotate = q.index(pick[i])
    rightRotate = len(q) - leftRotate
    if leftRotate < rightRotate:
        for i in range(leftRotate):
            q.append(q.popleft())
            cnt+=1
    else:
        for i in range(rightRotate):
            q.appendleft(q.pop())
            cnt+=1
    q.popleft()
print(cnt)
