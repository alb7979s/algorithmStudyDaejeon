from sys import*
input=stdin.readline
n=int(input())
a=list(map(int,input().split()))
b, c = map(int,input().split())
res=0
for i in range(n):
    res += 1
    a[i]-=b
    if a[i]>0:res += a[i]//c if a[i]%c==0 else a[i]//c+1
print(res)
