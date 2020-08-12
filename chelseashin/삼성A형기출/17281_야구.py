import sys
sys.stdin = open('17281_input.txt')

# 이닝별로 아웃카운트, 타자순서 관리(다음 이닝에 첫 타자 인덱스 유지)
# 점수 먼저 더해주고 선수 다음 베이스로 옮기기(순서 바꾸면 X)
# 변수별 초기화 위치 신경쓰기!
# 실수 금지!!!!
def play_games(order):
    global innings
    score = 0
    hitter_idx = 0
    for each_inning in innings:
        b1, b2, b3, = 0, 0, 0
        out_count = 0
        while out_count < 3:
            if each_inning[order[hitter_idx]] == 0:
                out_count += 1
            elif each_inning[order[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif each_inning[order[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif each_inning[order[hitter_idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif each_inning[order[hitter_idx]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            hitter_idx = (hitter_idx + 1) % 9
    return score

# 순열(dfs)로 라인업 구하기
def make_lineup(depth):
    global max_score, score
    if depth == 3:
        lineup.append(0)
        make_lineup(depth+1)
        lineup.pop()
    if depth == 9:
        # print(lineup)
        if play_games(lineup) > max_score:
            max_score = play_games(lineup)
        return
    for i in range(1, 9):
        if visited[i]:
            continue
        visited[i] = 1
        lineup.append(i)
        make_lineup(depth+1)
        lineup.pop()
        visited[i] = 0

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
# print(innings)

max_score = 0
lineup = []
visited = [0] * 9
make_lineup(0)
print(max_score)