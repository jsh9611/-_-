# 1095_Magic_Beads.py
S,F, M  = map(int, input().split())   

def factorial(num):
    if (num==1):
        return num
    else:
        res = num
        for i in range(1,num):
            res *= i
        return res

def factorial2(num,b):
    if (num==1):
        return num
    else:
        res = num
        for i in range(b,num):
            res *= i
        return res
    
# N = factorial(S+F)/factorial(S)*factorial(F)
N = factorial2(S+F,S+1)/factorial(F)

if M==1:
    print(1)
elif M>100000:
    print(-1)
else:
    for i in range(M,0,-1):
        if N % i == 0:
            print(i)
            break

# if N<=M:
#     print(M*(M//N))
# else:
#     print(-1)
