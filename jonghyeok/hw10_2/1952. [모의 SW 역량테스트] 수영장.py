INF=1e9
def solve(pos, price):
    res = INF
    if pos >= 12: return price
    #1일 처리
    res = min(res, solve(pos+1, price + (prices[0]*plans[pos])))
    for i in range(1, 4):
        res = min(res, solve(pos+p[i], price+prices[i]))
    return res
for tc in range(int(input())):
    p = [0, 1, 3, 12]
    prices = list(map(int,input().split()))
    plans = list(map(int,input().split()))
    print('#{} {}'.format(tc+1, solve(0, 0)))
