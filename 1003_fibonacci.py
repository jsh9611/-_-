count = int(input())
fibo_list = [[0 for i in range(2)] for j in range(41)] 

def fibo(n):
    for i in range(n+1):
        if i == 0:
            fibo_list[i][0] = 1
        elif i == 1:
            fibo_list[i][1] = 1
        else:
            fibo_list[i][0] = fibo_list[i-1][0] +fibo_list[i-2][0]
            fibo_list[i][1] = fibo_list[i-1][1] +fibo_list[i-2][1]
        if i == n:
            print(fibo_list[i][0], fibo_list[i][1])

for j in range(count):
    f_num = int(input())
    fibo(f_num)

"""
>>> t = [1, 5, 7, 33, 39, 52]
>>> for p in enumerate(t):
...     print(p)

"""