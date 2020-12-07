import sys
sys.stdin = open("2841_input.txt")
input = sys.stdin.readline

N, P = map(int, input().split())
D = dict()
move = 0
for _ in range(N):
    n, p = map(int, input().split())
    # n개의 줄마다 플랫 정보를 딕셔너리 값 부분에 스택으로 관리
    if n not in D.keys():
        D[n] = [p]
        move += 1
    else:
        # 이전에 눌린 플랫이 자신과 같은 수일 때
        if D[n][-1] == p:
            continue
        # 이전에 눌린 플랫이 자신보다 작을 때
        elif D[n][-1] < p:
            D[n].append(p)
            move += 1
            continue
        # 이전에 눌린 플랫이 자신보다 클 때
        while True:
            D[n].pop()
            move += 1
            if not D[n]:
                D[n].append(p)
                move += 1
                break
            if D[n][-1] == p:
                break
            elif D[n][-1] < p:
                D[n].append(p)
                move += 1
                break

    # print(n, p, D, move)
# print(D)

print(move)