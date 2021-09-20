#큰 수의 법칙-2
# M의 크기가 매우 클 경우 큰 수의 법칙-1은 시간초과가 발생한다.

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# n, m, k = 5, 8, 3
# data = [2, 4, 5 ,4 ,6]
n, m, k = 5, 7, 2
data = [3, 4, 3 ,4 ,3]

data.sort()
first_big = data[n-1]
second_big = data[n-2]

count2 = int(m/k)
count1 = m - count2

result = 0
result += count1 * first_big
result += count2 * second_big

print(result)