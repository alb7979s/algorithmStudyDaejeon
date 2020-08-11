#time over
from sys import*
from itertools import*
input=stdin.readline
def play():
    pos=0
    sum=0
    for i in range(n):
        base = [0]*4
        out = 0
        while 1:
            if out == 3: break
            state = a[i][turn[pos]]
            pos+=1
            if not state: out+=1
            else:
                for j in range(2, -1, -1):
                    if j + state >= 3:
                        base[3] += base[j]
                    else:
                        base[j+state] += base[j]
                    base[j] = 0
                base[state-1] += 1
            if pos==9: pos = 0
        sum += base[3]
    return sum
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
res=0
for perm in permutations(range(1, 9)):
    perm = list(perm)
    turn = perm[:3] + [0] + perm[3:]    #첫번째가 4번임
    res = max(res, play())
print(res)
