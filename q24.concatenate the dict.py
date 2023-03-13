# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# d={}
# for i in dic1:
#     if i not in d:
#         d.update({i:dic1[i]})
#     for j in dic2:
#         if j not in d:
#             d.update({j:dic2[j]})
#         for k in dic3:
#             if k not in d:
#                 d.update({k:dic3[k]})            
# print(d)



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d={}
for i in dic1:
    if i not in d:
        d.update({i:dic1[i]})
for j in dic2:
    if j not in d:
        d.update({j:dic2[j]})
for k in dic3:
    if k not in d:
        d.update({k:dic3[k]})            
print(d)
