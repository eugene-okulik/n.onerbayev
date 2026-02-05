
# Task1 Распакооука
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person


# Task2
a = "результат операции: 42"

strend = a.index(":") + 2

num = int(a[strend:])

print(num + 10)


b = "результат операции: 514"

strend = b.index(":") + 2

num = int(b[strend:])

print(num + 10)


c = "результат работы программы: 9"

strend = c.index(":") + 2

num = int(c[strend:])

print(num + 10)


# Task3
students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students = ", ".join(students)

subjects = ", ".join(subjects)

print(f'Students {students} study these subjects: {subjects}')
