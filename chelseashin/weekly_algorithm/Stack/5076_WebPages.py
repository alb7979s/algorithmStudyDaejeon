import sys
sys.stdin = open("5076_input.txt")

while True:
    code = input()
    if code == "#":
        break
    stack = []
    idx = 0
    for i in range(len(code)):
        if code[i] == "<":
            tag = ""
            idx = i+1
            while True:
                if code[idx] not in "</>":
                    tag += code[idx]
                idx += 1
                if code[idx] == ">":
                    break
            # print(tag)
            if tag == "br ":
                continue
            if tag[0] == "a":
                tag = "a"
            if not stack:
                stack.append(tag)
            else:
                if stack[-1] == tag:
                    stack.pop()
                else:
                    stack.append(tag)
    # print(stack)
    if stack:
        print("illegal")
    else:
        print("legal")