a=[{"first":"1"},  {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"}, {"seven":"7"}]
b=[]
for i in a:
    if type(i)==dict:
        for j in i:
            if i[j] not in b:
                b.append(i[j])
print(b)




