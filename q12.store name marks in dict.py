d={}
for i in range(11):
    name=input("enter name of student:")
    marks=int(input("enter marks of student:"))
    d.update({name:marks})
print(d)