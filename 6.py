n = int(input('Число'))
d = []
x = []
for i in range(n):
    x = str(input('Введи строку'))

    d += x.split(sep=' ')

b = []
for i in d:
    b.append(d.count(i))
v = dict(zip(d, b))

print(v)