def solution(id_list, report, k):
    report = list(set(report))
    len_a = len(id_list)
    count = [0]*len_a
    user_report = [[] for _ in range(len_a)]
    for item in report:
        han, bat = item.split()
        if bat in id_list:
            count[id_list.index(bat)] += 1
            user_report[id_list.index(han)].append(bat)
    ban = []
    for i in range(len_a):
        if count[i] >= k:
            ban.append(id_list[i])
    answer = [0]*len_a
    for i in range(len_a):
        for item in ban:
            if item in user_report[i]:
                answer[i] += 1
    return answer

# a = ["muzi", "frodo", "apeach", "neo"]
# b = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# c = 2
a = ["con", "ryan"]
b = ["ryan con", "ryan con", "ryan con", "ryan con"]
c = 3

print(solution(a,b,c))
# print(a1)
# print(a2)