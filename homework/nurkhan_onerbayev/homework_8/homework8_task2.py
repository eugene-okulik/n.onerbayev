import sys

sys.set_int_max_str_digits(1000000)


def fibonacci(limit=10):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


count = 1
needed_num = {5, 200, 1000, 100000}
max_fibo = max(needed_num)

for i in fibonacci(max_fibo):
    if count in needed_num:
        print(f"Число {count} = {i}")
    count += 1
