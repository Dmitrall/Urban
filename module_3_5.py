def get_multiplied_digits (number):
    str_number = str(number)
    res_str_number = str_number.strip("0")
    first = str(int(res_str_number[0]))
    res_first = int(first)


    if len(res_str_number) > 1:
        return res_first * get_multiplied_digits(int(res_str_number[1:]))

    elif len(res_str_number) <= 1:
        return res_first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
print(get_multiplied_digits(0402030)) #по словам преподавателя ноль должен убираться, почему ошибка, я не могу понять. Консультации не смог добиться
