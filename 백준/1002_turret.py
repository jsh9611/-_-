# 1002_turret.py
import math

count = int(input())

for i in range(count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 원점 사이의 거리
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