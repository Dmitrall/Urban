import random

number = random.randint(3, 20)
print(f"Случайное число: {number}")

pairs = ''

for i in range(1, 21):

    for j in range(i + 1, 21):
        if number % (i + j) == 0:
            pairs = pairs + str(i) + str(j)

print('Первое число:', number)
print('Второе число для вставки:', pairs, ' - пароль')
