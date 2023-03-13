a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
for i in range(len(a)):
    if type(a[i])==dict:
        for j in a[i]:
            a[i][j]=int(a[i][j])
print(a)



a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
for i in range(len(a)):
    if type(a[i])==dict:
        for j in a[i]:
            # a[i][j]=int(a[i][j])
            a[i][j]=float(a[i][j])
print(a) 
