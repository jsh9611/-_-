import sys
n, k = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    a = int(sys.stdin.readline())
    # 동전의 가치가 K초과이면 건너뛴다
    if a > k:
        continue
    arr.append(a)

arr_length = len(arr)
# 주어진 동전으로 k를 만들지 못하는 경우 0 출력
if arr_length == 0:
    print(0)
else:
    dp = [0]*k
    for i in range(arr_length):
        # 동전의 가치에 해당하는 위치에 1을 더해준다
        dp[arr[i]-1] += 1
        # 동전의 가치(arr[i])를 바꿔가면서 dp에 더해나간다
        for j in range(arr[i],k):
            dp[j] += dp[j-arr[i]]
print(dp[-1])