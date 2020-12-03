my_list = ['Hello, World! What a wonderful day?\n', 'London is the capital of Great Britain\n', 'Hello, World\n']

with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)

with open("test_2.txt") as file_obj:

    lines = file_obj.readlines()

    print(f'Строк в файле: {len(lines)}\n')

    for index, value in enumerate(lines):
        num_words = len(value.split())
        print('Строка {} имеет {} слов.\n'.format(index + 1, num_words))


