x1 = input('1 список: ')
x2 = input('2 список: ')

q1 = x1.split(sep=' ')
q2 = x2.split(sep=' ')
print(set(q1 + q2))