from sys import*
input=lambda:stdin.readline().strip()

n, k = map(int,input().split())
inp = input()
visit = {}
for i in range(n):
    if inp[i] == 'P':
        for j in range(i-k, i+k+1):
            if j<0 or j>n-1: continue
            if j not in visit and inp[j]=='H':
                visit[j] = 1
                break
print(len(visit))
