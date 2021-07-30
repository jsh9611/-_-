import sys
input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    if n==0 and a ==0 and b == 0:
        break

    balloons = []

    for i in range(n):
        balloons.append(list(map(int, input().split())))
    

    out = sorted(balloons, key = lambda x:(-abs(x[1]-x[2])))
    sum = 0

    for i in range(n):
        # a에서 더이상 가지고 올 수 없는 경우 b에서만 가지고 온다
        if a == 0:
            sum += out[i][0]*out[i][2]
        # b에서 더이상 가지고 올 수 없는 경우 a에서만 가지고 온다
        elif b == 0:
            sum += out[i][0]*out[i][1]
        else:
            # A가 더 큰 경우
            if out[i][1]>out[i][2]:
                if out[i][0] > b:
                    sum += b*out[i][2]
                    sum += (out[i][0]-b)*out[i][1]
                    b = 0
                else:
                    sum += out[i][0]*out[i][2]
                    b -= out[i][0]
            # B가 더 큰 경우
            elif out[i][1]<=out[i][2]:
                if out[i][0] > a:
                    sum += a*out[i][1]
                    sum += (out[i][0]-a)*out[i][2]
                    a = 0
                else:
                    sum += out[i][0]*out[i][1]
                    a -= out[i][0]
            # 절대값이 0인 경우
            else:
                a = 0
                b = 0
                sum += out[i][0]*out[i][1]
    print(sum)

"""
테스트케이스
3 15 35
10 20 10
10 10 30
10 40 10
2 10 10
10 1 3
10 1 2
0 0 0
"""
