dict1={"name":"Raju", "marks":56}
n=input("enter word:")
# if type(n)==str:
if n in dict1 and n=="name" or n=="Raju":
    print(n,"exist in dict.")
else:
    print(n,"dosen't exist in dict.")
