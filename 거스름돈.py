#그리디
#거스름돈. 동전 최소 개수
#500원, 100원, 50원, 10원

n = 1260 # 입력 받은 금액

'''
# 무식한 방법
c1 = n//500 #개수

l = n
l = l - 500*c1

c2 = l//100
l = l - 100*c2

c3 = l//50
l = l - 50*c3

c4 = l//10
l = l - 10*c4

print(c1)
print(c2)
print(c3)
print(c4)
print(c1+c2+c3+c4)
'''

# 반복문 사용
count = 0
money = n
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += money//coin
    money %= coin

print(count)