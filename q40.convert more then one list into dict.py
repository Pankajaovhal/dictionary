a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
l=[]
# d={}
for i in range(len(a)):
    d={}
    # d.update({a[i]:{b[i]:c[i]}})
    d.update({a[i]:{b[i]:c[i]}})
    # print(d)
    l.append(d)
print(l)
    

