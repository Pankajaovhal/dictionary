a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for i in a:
    if type(a[i])==list:
        a[i].clear()
        a[i]=[]
print(a)