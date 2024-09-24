def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ('Good day', 125, [1,2,3])
values_dict = {'a': 125, 'b':True, 'c': 'good night'}

values_list_2 = (1010, 'autumn')

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42) # a по идее не а, а - с