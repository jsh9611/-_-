# 1002_turret.py
import math

count = int(input())

for i in range(count):
    print('--------------')
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # r1이 더 크게 만들어 준다
    if r2>r1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1

    # 영점~중점 거리
    p1 = (x1**2+y1**2)**0.5
    p2 = (x2**2+y2**2)**0.5

    p2p = math.sqrt((x1-x2)**2+(y1-y2)**2)

    # 두 원이 같은 경우
    if p2p == 0 and r1==r2:
        print(-1)    
    # 원이 외접, 내접하는 경우 
    elif p2p == abs(r1 + r2) or p2p == abs(r2-r1):
        print(1)
    # 원이 두 점에서 만나는 경우
    elif abs(r1-r2) < p2p < abs(r1+r2):
        print(2)
    # 원이 서로 만나지 않는 경우
    else:
        print(0)
"""
    # r2원의 원점이 r1원 밖에 있는 경우
    if p2 > r1:
        print('case1')
    # if (x1^2+y1^2) ** 0.5 + r1 < (x2^2+y2^2) ** 0.5:
        if p2 - p1 > r1+r2:
            print(2)
            print('a')
            continue
        elif p2 - p1 == r1+r2:
            print(1)
            print('b')
            continue
        else:
            print(0)
            print('c')
            continue

    # r2원의 원점이 r1원 안에 있는 경우
    elif p2 < r1:
        print('case2')    
    # if (x1^2+y1^2) ** 0.5 + r1 > (x2^2+y2^2) ** 0.5:
        # 두 점에서 만날 때
        if p1 - p2 + r2 > r1:
            print(2)
            print('d')
            continue
        elif p1 - p2 + r2 < r1:
            print(0)
            print('e')
            continue
        else:
            print(1)
            print('f')
            continue
    if x1 == x2 and y1 == y2 and r1==r2:
        print(-1)
        continue

"""