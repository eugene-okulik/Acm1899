result1 = 'результат операции: 42'
index1 = result1.index(': ')
num1 = int(result1[index1+2:])
print(num1 + 10)

result2 = 'результат операции: 514'
index2 = result2.index(': ')
num2 = int(result2[index2+2:])
print(num2 + 10)

result3 = 'результат работы программы: 9'
index3 = result3.index(': ')
num3 = int(result3[index3+2:])
print(num3 + 10)
