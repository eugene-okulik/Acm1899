n = 10

while True:
    user_input = int(input('Введите цифру: '))
    if user_input == n:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
