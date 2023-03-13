d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
m=0
l=[]
for i in d:
    if d[i]>m:
        m=d[i]
        k=i
l.append(k)
# print(k)
# m2=0
# for i in d:
#     if d[i]>m2 :
#        if d[i]!=m:
#         m2=d[i]
#         k=i
# l.append(k)
print(l)