d={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in d:
    print(i,end=" ")
a=[]
for i in d:
    b=d[i]
    a.append(b)
print()
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=a[j][i]
        print(sum,end=" ")
        j+=1
    print()
    i+=1

