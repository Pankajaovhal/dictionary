list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
# d={}
# for i in list1:
#     for j in list2:
#         d[i]=j
#         list2.remove(j)
#         break
# print(d)

l=[]
i=0
while i<len(list1):
    l.append((list1[i],list2[i]))
    i+=1
# print(l)
d={}
d.update(l)
print(d)



# l=[1,2,3,4]
# l1=["one","two","three","four"]
# l2={}
# i=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         if i==j:
#             l2.update({l1[i]:l[i]})
#         j+=1
#     i+=1
# print(l2)