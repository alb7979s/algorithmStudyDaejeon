from collections import deque
N = 6
# N = int(input())
cards = deque([c for c in range(N, 0, -1)])
# print(cards)

while True:
    if len(cards) == 1:
        print(cards.pop())
        break
    cards.pop()
    cards.appendleft(cards.pop())
    # print(cards)