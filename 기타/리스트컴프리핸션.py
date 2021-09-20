numbers = []
for i in range(1,11):
  numbers.append(i)
print(numbers)

numbers2 = [i for i in range(1,11)]
print(numbers2)

numbers3 = [i for i in range(1,11) if i%2 == 1]
print(numbers3)

temp = [1,2,3,4]
numbers4 = [idx for idx, value in enumerate(temp) if value >= 2]
print(numbers4)