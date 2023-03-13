d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
66)}
b={}
for i in d:
    if d[i][0]>=6 and d[i][1]>=70:
        b.update({i:d[i]})
print(b)