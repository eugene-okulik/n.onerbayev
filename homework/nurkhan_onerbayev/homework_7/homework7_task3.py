# Task3

number1 = "результат операции: 42"

number2 = "результат операции: 54"

number3 = "результат работы программы: 209"

number4 = "результат: 2"

# Result1
def rise_result(response: str):
    result = response.split(':')
    return(int (result[-1]) + 10)

print(rise_result(number1))
print(rise_result(number2))
print(rise_result(number3))
print(rise_result(number4))
