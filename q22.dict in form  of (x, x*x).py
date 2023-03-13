d={}
n=int(input("enter number:"))
for i in range(1,n+1):
    if i>0:
        x=i*i
        d.update({i:x})
print(d)