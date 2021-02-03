#숫자 카드 게임
#여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

""" 
<input>
2 4
7 3 1 8
3 3 3 4
<output>
3
"""

"""
n, m = map(int, input().split())
result = -1
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    if data[0]>result:
        result = data[0]
print(result)
"""

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
