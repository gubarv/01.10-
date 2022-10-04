l1 = []
n1 = int(input("Введите число переменных в 1 списке: "))
for i in range(n1):
    l1.append(int(input('Введите число: ')))
l2 = []
n2 = int(input("Введите число переменных во 2 списке: "))
for i in range(n2):
    l2.append(int(input('Введите число: ')))
l1 += l2
dct = {}

for i in l1:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
for j in sorted(dct):
    print("'%d':%d" % (j, dct[j]))