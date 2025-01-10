def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings,1):
        position = file.tell()
        file.write(string + '\n')
        string_positions[(index, position)] = string
    return string_positions
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)