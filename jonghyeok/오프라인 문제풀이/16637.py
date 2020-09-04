from sys import*
from collections import*
input = lambda:stdin.readline().strip()
def cal2(n1, op, n2):
    if op == '+': return n1+n2
    if op == '-': return n1-n2
    if op == '*': return n1*n2
def cal():
    print(check, end=' ')
    q=deque()
    i=0
    while 1:
        if i==n: break
        if i%2 != 0 and check[i]:
            q.append(cal2(int(q.pop()), a[i], int(a[i+1])))
            i+=1
        else:
            q.append(a[i])
        i+=1
    while q:
        if len(q)==1: break
        q.appendleft(cal2(int(q.popleft()), q.popleft(), int(q.popleft())))
    print(q[0])
    return q[0]
def solve(pos):
    global res
    if pos >= n:return cal()
    check[pos]=1
    res = max(res, solve(pos+4))
    check[pos]=0
    res = max(res, solve(pos+2))
    return res
n=int(input())
res=int(-1e10)
check=[0]*n
a=input()
print(solve(1))
