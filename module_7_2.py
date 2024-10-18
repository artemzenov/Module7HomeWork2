def custom_write(file_name, strings):

    strings_position = dict()

    file = open(file_name, 'w+', encoding='utf-8')

    for num_string, string in enumerate(strings, 1):
        strings_position[(num_string, file.tell())] = string
        file.write(f'{string}\n')
    else:
        file.close()

    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)