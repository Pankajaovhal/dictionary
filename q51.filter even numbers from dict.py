# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in d:
#     l=[]
#     for j in d[i]:
#         if j%2==0:
#             l.append(j)
#             # print(j)
#             d[i]=l
# print(d)


d={'V': [1, 3,5], 'VI': [1, 5], 'VII': [2, 7, 9]}
for i in d:
    l=[]
    for j in d[i]:
        if j%2==0:
            l.append(j)
            # print(j)
        if j%2!=0:
            j=" "
            d[i]=l
print(d)