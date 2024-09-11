my_dict = {'Dima': 1991, 'Alina': 1988, 'Max': 1995}
print('Dict:', (my_dict))
print('Existing value:', (my_dict.get('Max')))
print('Not existing value:', (my_dict.get('Tony')))

my_dict.update({'Tom': 2000, 'Anna': 2001})
print('Deleted value:', (my_dict.pop('Dima')))
print('Modified dictionary:',  (my_dict))


my_set_ = {1, 1, 2, 2, 3, 5, True, True, False, 'Dima', 'Max', 'Dima'}
print('Set:', (my_set_))
my_set_.update({100, 'Ann'})
my_set_.remove('Dima')
print('Modified set:',(my_set_))