#큰 수의 법칙
# M, K가 1만 이하
#가장 큰 수와 그 다음으로 큰 수를 알아야 한다.

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

n, m, k = 5, 8, 3
data = [2, 4, 5 ,4 ,6]

data.sort()
first_big = data[n-1]
second_big = data[n-2]

result = 0
count = 0
for i in range(m):
    count += 1
    if count == k+1:
        result += second_big
        count = 0
        continue
    result += first_big
print(result)