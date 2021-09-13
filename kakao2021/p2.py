def change(n, b):
    if n < b:
        return str(n)
    s = change(n//b, b)
    return s + str(n%b)

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True

def is_prime(x):
    i = 2
    while i*i<x:
        if x%i == 0: return False
        else: i += 1
    return True

def solution(n, k):
    answer = 0
    # s = change(n,k).split('0')
    s = ''
    while n // k >= 1:
        remain = n % k
        n = n // k
        s = str(remain) + s
        if n < k :
            s = str(n) + s
    s = s.split('0')
    while '1' in s:
        s.remove('1')
    for item in s:
        if item == '':
            continue
        if is_prime_number(int(item)):
            answer += 1
    return answer

# print(solution(437674, 3))
print(solution(110011,10))