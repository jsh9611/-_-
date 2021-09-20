import sys
n = int(sys.stdin.readline())

time = []
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))
scd = sorted(time, key=lambda x: -x[1])  

# 0번째 끝나는 시간으로 ans 초기화
ans = scd[0][1]-scd[0][0]

for i in range(1,n):
    # 끝내야 하는 시간이 현재 시간보다 앞선 경우
    if ans>scd[i][1]:
        # i번째 일의 끝나는 시간을 기준으로 일한 만큼 빼서 갱신
        ans = scd[i][1]-scd[i][0]
    #  끝내야 하는 시간이 현재 시간보다 나중인 경우
    else:
        # 현재시간을 기준으로 일한 만큼 빼서 갱신
        ans = ans - scd[i][0]
print(ans if ans>=0 else -1)

"""
4
3 5
8 14
5 20
1 16
=>2

3
4 5
1 5
2 20
=>0

3
1 2
1 2
3 2
=>-1

3
1 1
2 2
3 3
=>-1
"""