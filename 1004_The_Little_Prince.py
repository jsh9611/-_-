# 1004_The_Little_Prince.py
"""
테스트 케이스 개수 : 2

출발점xy, 도착점xy : -5 1 12 1
행성계의 개수 : 7
행성 중점xy, 반지름r : 1 1 8
                    -3 -1 1
                    2 2 2
                    5 5 1
                    -4 5 1
                    12 1 1
                    12 1 2

출발점xy, 도착점xy : 5 1 5 1
행성계의 개수 : 1
행성 중점xy, 반지름r : 0 0 2
"""
import math

# 출발점과 도착점의 p2p < r 인 경우를 각각 더한다
T = int(input())
f = []
for i in range(T):
    # 출발점(x1,y1), 도착점(x2,y2)
    x1, y1, x2, y2 = map(int, input().split())
    # 행성계의 개수
    P = int(input())
    count = 0
    for i in range(P):
        # 행성 중점과 반지름 x3,y3,r 
        x3, y3, r3 = map(int, input().split())
        o1 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
        o2 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
        # 출발점과 도착점 모두 행성 궤도 안에 있는 경우
        if (o1 < r3 and o2 < r3):
            continue
        # 출발점만 행성 궤도에 갇힌 경우
        if (o1 < r3):
            count += 1
        # 도착점만 행성 궤도에 갇힌 경우
        if (o2 < r3):
            count += 1
    print(count)