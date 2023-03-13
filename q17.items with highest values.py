my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
m1=[]
m2=[]
m3=[]
for i in my_dict:
    if my_dict[i]>m1:
        m1=i
    if my_dict[i]>m2 and my_dict[i]!=m1:
        m2=i
# for i in my_dict:
#     if my_dict[i]>m3 and my_dict[i]!=m2 and my_dict[i]!=m1:
#         m3=my_dict
print(m1,m2,m3)    
