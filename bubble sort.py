# # Creating a bubble sort function  
# def bubble_sort(list1):  
#     # Outer loop for traverse the entire list  
#     for i in range(0,len(list1)-1):  
#         for j in range(len(list1)-1):  
#             if(list1[j]>list1[j+1]):  
#                 temp = list1[j]  
#                 list1[j] = list1[j+1]  
#                 list1[j+1] = temp  
#     return list1  
  
# list1 = [5, 3, 8, 6, 7, 2]  
# print("The unsorted list is: ", list1)  
# # Calling the bubble sort function  
# print("The sorted list is: ", bubble_sort(list1))   


d={"apple":2,"ball":1,"dog":6,"gun":9,"hat":3}
a=[]
c={}
for i in d:
    a.append(d[i])
for j in range(len(a)):
    for k in range(len(a)-1):
        if a[k]>a[k+1]:
            t=a[k]
            a[k]=a[k+1]
            a[k+1]=t
for m in range(len(a)):
    for l in d:
        if d[l]==a[m]:
            c.update({d[l]:l})
print(c)

