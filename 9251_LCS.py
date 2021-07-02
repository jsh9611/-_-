# 9251_LCS.py
s1 = input()
s2 = input()

len_a = len(s1)
len_b = len(s2)

lcs_list = [[0 for i in range(len_a+1)] for j in range(len_b+1)]
count = 0

for i in range(1,len_b+1):
    for j in range(1,len_a+1):
        if s2[i-1] == s1[j-1]:
            lcs_list[i][j] = lcs_list[i-1][j-1] + 1
        else:
            lcs_list[i][j] = max(lcs_list[i-1][j], lcs_list[i][j-1])
            
for i in range(len_b,0,-1):
    for j in range(len_a,0,-1):
        if lcs_list[i-1][j] == lcs_list[i][j-1] == lcs_list[i][j]:
            break
        elif lcs_list[i-1][j] == lcs_list[i][j-1]:
            count += 1
            break
        else:
            continue
print(count)



# for j in range(1,len_b):
#     for i in range(skip,len_a):
#         print(i,j)
#         if lcs_list[i][j] == 1:
#             print(999,i,j)
#             count += 1
#             skip = i+1
#             break
# print(count)