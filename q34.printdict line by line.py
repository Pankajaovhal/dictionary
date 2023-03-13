# s = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i in s:
#     print(i)
#     for j in s[i]:
#         # print(i)
#         print(j)



# a={"a":1,"b":2,"c":{"a":5,"b":{"d":11}}}
# for i in a:
#     if type(a[i])==int:
#         print(a[i],end=",")
# # for j in a[i]:
# #     if type(a[i][j])==int:
# #         print(a[i][j])
# # for k in a[i][j]:
# #     if type(a[i][j][k])==int:
# #         print(a[i][j][k])


n=["pankaja","jyothsna","shivani"]
s=["ovhal","devi","singh"]
a=[17,25,19]
d=[]
f={}
for i in range(len(n)):
    d.append(n[i])
    f.update({"s":s[i],"a":a[i]})
    g={}
    for j in f:
        g.update({d[i]:{j}})
print(g)
# print(d)
# print(f)
# g={}
# for j in d:
#     g.update({j:f[i]})
# print(g)