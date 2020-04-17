documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def doc_name():
    while True:
        user_input = input('\nВведите номер документа: ')
        for m in documents:
            if user_input == m['number']:
                print(m['name'])
                break
        if user_input not in m['number']:
            print('Документа не найдено')
        break


def doc_all():
    for i in documents:
        y = list(i.values())
        print(f'{y[0]} {y[1]} {y[2]}')


def new_doc_name():
    # try:
    #     for i in documents:                                           для проверки исключения KeyError
    #         del i['name']
    #         print(i['name'])
    # except KeyError:
    #     print("Отсутствует поле имени документа")
    try:
        for j in documents:
            z = list(j.values())
            print(f'{z[2]}')
    except KeyError:
        print("Отсутствует поле имени документа")

def doc_direct():
    director = list(directories)
    while True:
        user_input = input('\nВведите номер документа: ')
        if user_input in directories['1']:
            print(director[0])
        elif user_input in directories['2']:
            print(director[1])
        elif user_input in directories['3']:
            print(director[2])
        elif user_input not in directories:
            print('Необходимо ввести только цифры, являющиеся номером документа!')
        break


def new_doc():
    new_document_left = ['type', 'number', 'name']
    new_document_right = []
    while True:
        user_input = input('\nВведите тип документа: ')
        if user_input.isnumeric():
            print('Введите символьное (буквенное) обозначение!')
            continue
        else:
            new_document_right.append(user_input)

        user_input = input('Введите номер документа: ')
        if user_input.isnumeric():
            new_document_right.append(user_input)
        else:
            print('Введите номер (цифры)!')
            continue

        user_input = input('Введите имя владельца документа: \n')
        if user_input.isnumeric():
            print('Введите символьное (буквенное) обозначение!')
            continue
        else:
            new_document_right.append(user_input)
            new_document_full = dict(zip(new_document_left, new_document_right))
            documents.append(new_document_full)
        print(documents)
        break


def num_dir():
    print('\nСписок всех имеющихся полок: ')
    for n, in directories:
        print(n)
    while True:
        user_input = input('\nВведите номер полки для хранения: ')
        a = documents[-1]['number']
        if user_input in directories.keys():
            directories[user_input].append(a)
            print(directories[user_input])
        elif not user_input.isnumeric():
            print('Введите номер(цифры)!')
            continue
        elif user_input not in directories.keys():
            directories[user_input] = []
            directories[user_input].append(a)
            print(directories)
        break


def main():
    print('p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;'
          '\nl – команда, которая выведет список всех документов;'
          '\ns – команда, которая спросит номер документа и выведет номер полки, на которой он находится;'
          '\na – команда, которая добавит новый документ в каталог и в перечень полок; '
          '\nn - команда, которая проверит наличие поля имени.')
    while True:
        user_input = input('\nВведите команду: ')
        if user_input == 'p':
            doc_name()
        elif user_input == 'l':
            print('\nСписок всех документов:\n')
            doc_all()
        elif user_input == 's':
            doc_direct()
        elif user_input == 'a':
            new_doc()
            num_dir()
        elif user_input.isnumeric():
            print('Введите команды, предложенные выше!')
        elif user_input == 'n':
            new_doc_name()
        elif user_input == 'q':
            break


main()



