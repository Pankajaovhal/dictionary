a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
b=[]
for i in a:
    if type(i)==dict:
        for j in i:
            if i[j] not in b:
                b.append(i[j])
print(b)


# a=[1,2,3,4,5,15]
# i=0
# while i<len(a):
#     if a[i]%3==0:
#         a.remove(a[i])
#         a.insert()
