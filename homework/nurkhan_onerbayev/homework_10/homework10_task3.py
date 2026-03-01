def operation_control(func):

    def wrapper(first, second):
        
        if first < 0 or second < 0:
            operation = '*'
        
        elif first == second:
            operation = '+'
        
        elif first > second:
            operation = '-'
        
        else:
            operation = '/'
        
        return func(first, second, operation)

    return wrapper


@operation_control
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = calc(a, b)
print("Результат:", result)
