l={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# for i,j in l.items():
#     if j in l.values():
#         count+=1
# # print("key","value","count")
#         print(i,j,count)

count=0
for i in l:
    count+=1
    print(i,l[i],count)
