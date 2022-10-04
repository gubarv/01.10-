l = []
n = int(input("Введите число переменных: "))
for i in range(n):
    l.append(int(input('Введите число: ')))
print(f'В списке {len(set(l))} различных цифр')