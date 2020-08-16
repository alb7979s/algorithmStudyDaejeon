from sys import*
from collections import*
input=lambda:stdin.readline().strip()
def solve():
    lastMove = -1
    comP, arrP, strP = 0, 0, 0 #commandPointer, arrPointer, stringPointer
    for i in range(int(5e7)+1):
        if comP == comSize: return 'Terminates'
        state = command[comP]
        # -, + 일 때 overflow, underflow 체크 
        if state =='-': arr[arrP] = (arr[arrP] + 255)%256
        elif state == '+': arr[arrP] = (arr[arrP] + 1)%256
        elif state == '<': arrP = (arrP - 1 + arrSize) % arrSize
        elif state == '>': arrP = (arrP + 1) % arrSize
        elif state == '[' and not arr[arrP]:
            comP = jump[comP]
        elif state == ']' and arr[arrP]:
            lastMove = max(lastMove, comP)
            comP = jump[comP]
        elif state == ',':
            if strP >= strSize: arr[arrP] = 255
            else: arr[arrP] = ord(string[strP])
            strP += 1
        comP += 1
    return 'Loops {} {}'.format(jump[lastMove],lastMove)
for tc in range(int(input())):
    arrSize, comSize, strSize = map(int,input().split())
    command = input()
    string = input()
    jump = {}
    arr = [0] * arrSize
    st=[]
    #jump 구간 설정
    for i in range(comSize):
        if command[i] == '[':
            st.append(i)
        elif command[i] == ']':
            x = st.pop()
            jump[x] = i
            jump[i] = x
    print(solve())
