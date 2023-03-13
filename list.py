# i=0
# sum=1
# while i<5:
#     sum=sum+i
#     i=i+1
# print(sum)


# a={1:2,3:4,5:6}
# for i in a:
#     print({i:a[i]})


# d={"a":3,"b":4,"c":6}
# n=input("enter word:")
# u=d.fromkeys(d)
# if n in u:
#     print("exiest")
# else:
#     print("not")


d={1:4,2:7,3:9,4:12,5:16}
l=[]
for i in d:
    l.append(d[i])
    c=0
    while c<len(l):
        if l[c]%2==0:
            print(c)
        c+=1
