import sys
sys.stdin = open("20055_input.txt")

# 시험장 풀이 - 메모리, 시간 최적화

N, K = map(int, input().split())
belt = list(map(int, input().split()))

robot = [0] * 2 * N
zeroCnt = 0
time = 0
while True:
    # 1
    time += 1
    belt = [belt[-1]] + belt[:-1]
    robot = [0] + robot[:-1]
    robot[N-1] = 0
    # 2
    for i in range(N-2, -1, -1):
        if robot[i]:
            if not robot[i+1] and belt[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    zeroCnt += 1
    robot[N-1] = 0
    # 3
    if belt[0] > 0 and not robot[0]:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            zeroCnt += 1
    # 4
    if zeroCnt >= K:
        print(time)
        break