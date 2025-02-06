import random

salary = int(input('Enter salary: '))
new_salary = salary
bonus = random.choice([True, False])
bonus_rate = random.randrange(0, 10001)
if bonus == True:
    new_salary = salary + bonus_rate
print(f"{salary}, {bonus} - '${new_salary}'")