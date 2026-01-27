
# Task1 Распакооука
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person


# Task2 
a = "результат операции: 42"

a = a.split(':')

num = a[-1]

num = int(num.strip())

print(num + 10)


b = "результат операции: 514"

b = b.split(':')

numb = b[-1]

numb = int(numb.strip())

print(numb + 10)


c = "результат работы программы: 9"

c = c.split(':')

numc = c[-1]

numc = int(numc.strip())

print(numc + 10)


# Task3
students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students = ", ".join(students)

subjects = ", ".join(subjects)

print(f'Students {students} study these subjects: {subjects}')