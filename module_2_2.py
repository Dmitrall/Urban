number_first = int(input('Введите число 1: '))
number_second = int(input('Введите число 2: '))
number_third = int(input('Введите число 3: '))

if number_first == number_second == number_third:
    print('3' )
elif number_first == number_second or number_first == number_third or number_second == number_third:
    print('2')
else:
    print('0')
