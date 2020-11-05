from sys import*
input=lambda:stdin.readline().strip()
for tc in range(int(input())):
    L = input()
    left, right = [], []
    for i in range(len(L)):
        if L[i] == '<':
            if left: right.append(left.pop())
        elif L[i] == '>':
            if right: left.append(right.pop())
        elif L[i] == '-':
            if left: left.pop()
        else:
            left.append(L[i])
    print(''.join(left)+''.join(right[::-1]))
