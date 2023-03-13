# d={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacharySimon']}
# b={}
# l=[]
# for i in d:
#     for j in d[i]:
#         b.update({i:j})
# l.append(b)
# print(l)


i=0
d={}
while i<2:
    a=int(input("enter number of item:"))
    d.update({a:{}})
    # j=0
    # while j<i:
    n=input("enter name:")
    age=int(input("enter age:"))
    d.update({a:{"name":n,"age":age}})
        # j+=1
    i+=1
print(d)