# a={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
a={2:0,1:3,4:2,3:1}
l=[]
for i in a:
    l.append(i)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            tem=l[j]
            l[j]=l[j+1]
            l[j+1]=tem
print(l)
b={}
for i in range(len(l)):
    for j in a:
        if l[i]==j:
            b.update({j:a[j]})
print(b)
{1:3,2:0,3:1,4:2}


# l=[]
# for i in a.values():
#     l.append(i)
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j]>l[j+1]:
#             tem=l[j]
#             l[j]=l[j+1]
#             l[j+1]=tem
# # print(l)
# # b={}  
# for i in range(len(l)):
#     for k in a.keys():
#       print(k,':',l[i])
#             # b.update({j:a})
# # print(b)