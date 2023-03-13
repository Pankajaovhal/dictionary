my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
m1=0
m2=0
m3=0
for i in my_dict:
    # print(my_dict[i])
    if my_dict[i]>m1:
        m1=my_dict[i]
    if my_dict[i]>m2:
        if my_dict[i]>m2 and my_dict[i]!=m1:
            m2=my_dict[i]
# for i in my_dict:
    if my_dict[i]>m3 and my_dict[i]!=m2 and my_dict[i]!=m1:
        m3=my_dict
print(m1,m2,m3) 
