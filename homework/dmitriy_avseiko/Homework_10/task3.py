def operator(func):

    def wrapper(*args):
        if first < 0 or second < 0:
            return func(*args, operation='*')
        elif first > second:
            return func(*args, operation='-')
        elif second > first:
            return func(*args, operation='/')
        elif first == second:
            return func(*args, operation='+')
    return wrapper


@operator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

print(calc(first, second))
