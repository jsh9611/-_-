# 1이 될 때 까지
# 두 과정 중 하나를 반복적으로 선택하여 수행한다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.(단 N이 K로 나누어떨어질 때만 선택 가능)
"""
#n이 k로 나누어떨어질때만 고려했음. 오답
n, k = map(int, input().split())
result = 0
if n%k == 0:
    while n != 1:
        if n<k:
            break
        result += 1    
        n /= k
else:
    result = n-1
print(result)

"""
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k # k로 나눌 수 있는 최대의 수
    result += (n-target) # 나머지 만큼 더한다. 1을 빼는 과정
    n = target
    # 더 이상 나눌 수 없을때
    if n<k:
        break
    n //= k
    result += 1
# 남은 n만큼의 횟수를 더해준다.
result += (n-1)
print(result)