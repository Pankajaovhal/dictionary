# Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d1:
    if i in d2:
        d2[i]=d2[i]+d1[i]
for i in d1:
    if i not in d2:
        d2.update({i:d1[i]})
# for i in d1:
#     if i in d2:
#         d1[i]=d2[i]+d1[i]
print(d2)

# for i in d2:
#     if i in d1:
#         d1[i]=d2[i]+d1[i]
# for i in d2:
#     if i not in d1:
#         d1.update({i:d2[i]})
# print(d1)


