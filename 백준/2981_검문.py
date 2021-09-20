import sys
sys.setrecursionlimit(100000)

def gcd(a, b):
    if a>b:
        a,b=b,a
    while b>0:
        temp = a
        a = b
        b = temp%b
    return a

def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)
            if (i != (n // i)): 
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]

n = int(sys.stdin.readline())

nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

val = 1000000001
if n == 2:
    val = nums[1]-nums[0]
else:
    for i in range(1,n-1):
        a = gcd(nums[i]-nums[0], nums[i+1]-nums[0])
        if a<val:
            val = a

for item in get_divisor(val):
    if item == 1:
        continue
    print(item, end=' ')