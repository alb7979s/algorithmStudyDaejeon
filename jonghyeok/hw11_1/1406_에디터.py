#1.스택 2개 이용
from sys import*
input=lambda:stdin.readline().strip()
L=input()
left, right = [], []
for i in range(len(L)):
    left.append(L[i])
for i in range(int(input())):
    inp = list(map(str,input().split()))
    if inp[0] == 'L':   #커서 왼쪽으로
        if left: right.append(left.pop())
    elif inp[0] == 'D': #커서 오른쪽
        if right: left.append(right.pop())
    elif inp[0] == 'P':
        left.append(inp[1])
    else:
        if left: left.pop()
print(''.join(left + right[::-1]))
        

#2. LinkedList 직접 구현
'''
from sys import *

setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self, value=None):
        self.prev = None
        self.nxt = None
        self.value = value
class LL:
    def __init__(self, mkString):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.pointer = self.head
        for i in range(len(mkString)):
            self.add(mkString[i])

    def add(self, value):
        self.temp = Node(value)
        self.pointer.nxt.prev = self.temp
        self.temp.nxt = self.pointer.nxt
        self.pointer.nxt = self.temp
        self.temp.prev = self.pointer
        self.pointer = self.pointer.nxt
    def left(self):
        if self.pointer != self.head:
            self.pointer = self.pointer.prev
    def right(self):
        if self.pointer.nxt != self.tail:
            self.pointer = self.pointer.nxt
    def remove(self):
        if self.pointer != self.head:
            self.pointer.prev.nxt = self.pointer.nxt
            self.pointer.nxt.prev = self.pointer.prev
            self.pointer = self.pointer.prev
    #__str__이랑 pointer 안바뀌게 temp쓰는거 배워가자
    def __str__(self):
        temp = self.pointer
        ans=''
        while temp.prev:
            temp = temp.prev
        while temp.nxt != self.tail:
            temp = temp.nxt
            ans += temp.value
        return ans
a = input()
ll = LL(a)
n = int(input())
for i in range(n):
    inp = list(map(str, input().split()))
    if inp[0] == 'L':
        ll.left()
    elif inp[0] == 'D':
        ll.right()
    elif inp[0] == 'B':
        ll.remove()
    else:
        ll.add(inp[1])
print(ll)
'''
