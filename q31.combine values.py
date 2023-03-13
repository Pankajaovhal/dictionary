a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
'amount': 750}]
s={}
for i in a:
    if i ["item"] not in s:
        s[i["item"]]=i["amount"]
    else:
        s[i['item']] += i['amount'] 
print(s)
