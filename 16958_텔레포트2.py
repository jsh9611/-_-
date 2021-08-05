import sys

n,t= map(int, sys.stdin.readline().split())

INF = 2000000000

city = []

for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

# 맨해튼 거리를 구한다
def direct(a, b):
    return abs(city[a][1] - city[b][1]) + abs(city[a][2] - city[b][2])

# 1. 일반도시 출발
# 바로 가는 경우와 특별 도시를 거쳐 텔레포트를 하는 경우가 있다.
# 각 도시간의 거리의 최소값을 via에 저장한다.
# 이때 일반도시에서 가장 가까운 특별 도시의 거리를 저장한다.
# 출발지점으로 부터 가장 가까운 특별도시의 거리와 
# 도착지점으로부터 가장 가까운 특별도시의 거리에 텔레포트 거리 t를 더하여 구한다.

# 2. 특별도시 출발
# 바로 가는 경우와 특별도시에서 특별도시(텔레포트)로 가는 경우가 있다.
# 특별도시인 경우 via는 0이 된다.

# 특별도시까지의 가장 가까운 거리를 구한다.
via = [0]*n
for i in range(n):
    # 자기 자신이 특별도시인 경우는 via[i]를 0으로 한다
    if city[i][0] == 1:
        continue
    via[i] = INF
    for j in range(n):
        # 일반 - 일반인 경우는 무시한다.
        if city[j][0] == 0:
            continue
        via[i] = min(via[i], direct(i,j))
    if via[i] == INF:
        via[i] = 0

m = int(sys.stdin.readline())
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    answer = min(direct(a-1,b-1), via[a-1] + t + via[b-1])
    
    # 둘 다 특별도시인 경우
    if city[a-1][0] == 1 and city[b-1][0] == 1:
        # 텔레포트를 사용한 것과 경유해서 가는 것의 거리를 비교한다.
        print(min(answer,t))
    else:
        # 직접 가는 경우와 (일반 -> 특별 -> 특별 -> 일반)인 경우를 비교한다.
        print(answer)