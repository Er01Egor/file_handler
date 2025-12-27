import sys

try:
    print('Выберите действие: 1) создать файл; 2) открыть существующий')
    input_ = int(input('Выберите число, соответсвующее вашему выбору (1 или 2): '))
    if input_ == 2:
        try:
            file_name = input('Введите имя файла: ')
            # text = input('Введите текст: ')
            print(f'Что сделать с файлом "{file_name}"')
            print('1) прочитать; 2) изменить')
            input_num = int(input('Выберите число, соответсвующее вашему выбору (1 или 2): '))
            if input_num == 1:
                content_file = []
                with open(file_name, 'r', encoding='utf-8') as file:
                    print(f'Содержание файла "{file_name}":')
                    content_file.append('--------- Начало файла ----------')
                    content_file.append(file.read())
                    content_file.append('--------- Конец файла ----------')
                for line in content_file:
                    print(line)
            if input_num == 2:
                print(f'Что записать в файл "{file_name}"')
                print('Введите текст (нажмите CTRL + D что бы остановить ввод): ')
                content_file = list(map(str, sys.stdin))
                with open(file_name, 'a', encoding='utf-8') as file:
                    for line in content_file:
                        result = line.strip('\n')
                        val = file.write(result + '\n')
        except FileNotFoundError:
            print(f'Файл с именем: "{file_name}" отсутствовал')

    if input_ == 1:
        file_name = input('Введите имя нового файла: ')

        print(f'Что записать в файл "{file_name}"')
        print('Введите текст (нажмите CTRL + D что бы остановить ввод): ')
        content_file = list(map(str, sys.stdin))
        with open(file_name, 'w', encoding='utf-8') as file:
            # content_file = content_file
            for line in content_file:
                result = line.strip('\n')
                val = file.write(result + '\n')


except Exception as err:
    print(f'Произошла ошибка: {err}')
