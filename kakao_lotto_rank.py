# 문제출처 : 프로그래머스(로또의 최고 순위와 최저 순위)
def solution(lottos, win_nums):
    mollu = 0
    good = 0
    for item in lottos:
        if item == 0:
            mollu += 1
        elif item in win_nums:
            good += 1
    best = 7-(good+mollu)
    if best > 6:
        best = 6
    worst = 7-good
    if worst > 6:
        worst = 6

    answer = [best, worst]
    return answer

# 입력부분
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solution(a,b))