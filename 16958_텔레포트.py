# 플루이드 와샬
import sys

n,t= map(int, sys.stdin.readline().split())

INF = 2000000000

city = []

for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

travel = [[INF]*n for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        distance = abs(city[i][1] - city[j][1]) + abs(city[i][2] - city[j][2])
        if city[i][0] == 1 and city[j][0] == 1:
            distance = min(distance, t)
            travel[i][j] = travel[j][i] = distance
        else:
            travel[i][j] = travel[j][i] = distance

# k = 거쳐가는 노드
for k in range(n):
    # i = 출발 노드
    for i in range(n):
        # j = 도착 노드
        for j in range(n):
            if travel[i][j] > travel[i][k] + travel[k][j]:
                travel[i][j] = travel[i][k] + travel[k][j]
s = ''
m = int(sys.stdin.readline())
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    s += (str(travel[a-1][b-1]) + '\n')
print(s)


