import sys
sys.stdin = open("3986_input.txt")
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    words = input()
    stack = []
    for word in words:
        # print(word)
        if word == '\n':
            break
        if not stack:
            stack.append(word)
        else:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
    if not stack:
        cnt += 1
print(cnt)