documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def ask_number_document():
    number_document = input('Введите номер документа: ')
    return number_document


def get_name_by_doc():
    number_document = ask_number_document()
    for doc in documents:
        if doc['number'] == number_document:
            return f"Имя владельца: {doc['name']}"

    return 'имя не найдено'


def get_number_shelf(number_document_param=None):
    number_document = number_document_param
    if not number_document_param:
        number_document = ask_number_document()

    for key, shelf in directories.items():
        if number_document in shelf:
            return key


def get_all_documents():
    list_documents = []
    for doc in documents:
        list_documents += [f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"']
    return list_documents


def add_document():
    number_document = ask_number_document()
    type_document = input('Введите тип документа: ')
    name_people = input('Введите имя владельца')
    number_shelf = input('Введите номер полки')
    new_document = {'type': type_document, 'number': number_document, 'name': name_people}
    documents.append(new_document)
    if number_shelf in directories.keys():
        directories[number_shelf].append(number_document)
        print('Документ успешкно добавлен')
    else:
        print('Такой полки не существует')


def delete_document():
    number_document = ask_number_document()
    for index, doc in enumerate(documents):
        if doc['number'] == number_document:
            removed_doc = documents.pop(index)
            print(f'Удалён следующий документ: {removed_doc}')
            break
    current_shelf = get_number_shelf(number_document)
    if current_shelf:
        directories[current_shelf].remove(number_document)
        print(f'Документ {number_document} успешно удалён')
    else:
        print(f'Полка с документом {number_document} не обнаружена')


def is_shelf_exist_in_dir(shelf):
    return shelf in directories.keys()


def move_document():
    number_document = ask_number_document()
    current_shelf = get_number_shelf(number_document)
    number_shelf = input('Введите номер полки, куда нужно перенести')
    if current_shelf and is_shelf_exist_in_dir(number_shelf):
        directories[current_shelf].remove(number_document)
        directories[number_shelf].append(number_document)
        print('Перемещение документа выполнено')

    else:
        print('Номер документа или полки не найден')


def add_shelf():
    number_shelf = input('Введите номер новой полки: ')
    if is_shelf_exist_in_dir(number_shelf):
        print('Такая полка уже существует')
    else:
        directories[number_shelf] = []
        print("Новая полка успешно создана")


def get_command():
    command = input("""p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.

Введите пользовательскую команду: """)
    if command == 'p':
        print(get_name_by_doc())
    elif command == 's':
        key = get_number_shelf()
        if key:
            print(f'Номер полки: {key}')
        else:
            print('Полка не найдена')

    elif command == 'l':
        print(get_all_documents())
    elif command == 'a':
        add_document()
    elif command == 'd':
        delete_document()
    elif command == 'm':
        move_document()
    elif command == 'as':
        add_shelf()
    else:
        print('Команда не найдена')
    clear = "\n" * 5
    print(clear)

    get_command()


get_command()