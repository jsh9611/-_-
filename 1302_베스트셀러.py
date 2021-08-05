n = int(input())

dict = {}

for i in range(n):
    name = input()
    dict.setdefault(name, 0)
    dict[name] += 1
print(sorted([key for key in dict.keys() if dict[key] == max(dict.values())])[0])