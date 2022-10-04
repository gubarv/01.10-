motherland = {}
for i in range(int(input("Колличество областей: "))):
    country, *cities = input("Введите область и города через пробел: ").split()
    for city in cities:
        motherland[city] = country

for i in range(int(input("Сколько ищем городков? "))):
    print(motherland[input("Какой город ищем? ")])