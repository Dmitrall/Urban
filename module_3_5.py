def get_multiplied_digits (number):
    str_number = str(number)
    res_str_number = str_number.strip('0')

    if len(res_str_number) > 1:
        res_first = int(res_str_number[0])
        return res_first * get_multiplied_digits(int(res_str_number[1:]))

    else:
        return int(str_number)

print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
print(get_multiplied_digits('0402030'))
print(get_multiplied_digits(0))
