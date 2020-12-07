import sys
sys.stdin = open("5397_input.txt")

T = int(input())
for tc in range(T):
    L = input()
    # 스택 2개 이용
    left, right = [], []
    for i in range(len(L)):
        if L[i] == "<":
            if left:
                right.append(left.pop())
        elif L[i] == ">":
            if right:
                left.append(right.pop())
        elif L[i] == "-":
            if left:
                left.pop()
        else:
            left.append(L[i])
    print(''.join(left + right[::-1]))