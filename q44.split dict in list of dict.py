d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l=[]
for i in d:
    b={}
    for j in d[i]:
        b.update({i:j})
        l.append(b)
print(l)