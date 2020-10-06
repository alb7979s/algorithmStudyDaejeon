import sys
sys.stdin = open('4008_input.txt')

def perm(depth):
    global MIN, MAX
    if depth == N-1:
        temp = numbers[0]
        for j in range(N-1):
            if order[j] == "+":
                temp += numbers[j+1]
            elif order[j] == "-":
                temp -= numbers[j+1]
            elif order[j] == "*":
                temp *= numbers[j+1]
            else:
                temp = int(temp / numbers[j+1])
        MIN = min(MIN, temp)
        MAX = max(MAX, temp)
        return

    for i in range(4):
        if not operators[i]:
            continue
        operators[i] -= 1
        order.append(oper[i])
        perm(depth+1)
        order.pop()
        operators[i] += 1

# main
T = int(input())
for tc in range(T):
    N = int(input())
    oper = "+-*/"
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    MIN = float('inf')
    MAX = float('-inf')

    order = []
    perm(0)
    print("#{} {}".format(tc+1, MAX-MIN))

    # 1 24
    # 2 8
    # 3 144
    # 4 8
    # 5 91
    # 6 150
    # 7 198
    # 8 2160
    # 9 46652
    # 10 701696