# 2110_Router_Installation.py
import sys

N, C = map(int, sys.stdin.readline().split())
router = [0]*N
for i in range(N):
    router[i] = int(sys.stdin.readline())
router.sort()

# 집과 공유기의 거리가 최대가 되는 경우
max = (router[-1]-router[0]) // (C-1)

while True:
    # router의 N개 주소에 대해 max이상인 주소들의 개수 확인
    left = 0
    count = 1
    for right in range(1,N):
        if router[right] - router[left] >= max:
            count += 1
            left = right
    # C개 이상 설치를 못한 경우 max 값에 1을 빼서 반복
    if count>=C:
        break
    else:
        max -= 1

print(max)