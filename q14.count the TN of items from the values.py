dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for i in dict1:
    for j in dict1[i]:
        c=c+1
print(c)