result = 'результат операции: 2'


def increase_value(result):
    index = result.index(': ')
    num = int(result[index + 2:])
    print(num + 10)


increase_value(result)
