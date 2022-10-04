students = [{input("Язык: ") for j in range(int(input('Число языков: ')))} for i in range(int(input("Колличество учеников: ")))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')