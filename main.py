documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# #проверка существования документа
# def check_document_number(user_doc_number):
#     doc_founded = False
#     for document in documents:
#         doc_number = document["number"]  #завожу переменную для хранения существующего номера документа
#         if doc_number == user_doc_number:
#             doc_founded = True
#             break
#     return doc_founded
#
# #проверка существования полки
# def check_shelf_number(user_shelf_number):
#     shelf_founded = False
#     for directory in directories:
#         shelf_number = directory[0]
#         if shelf_number == user_shelf_number:
#             shelf_founded = True
#             break
#     return shelf_founded
#
# #удалить документ с полки
# def remove_doc_from_shelf(user_doc_number):
#     for directory_number, directory_docs_list in directories.items():
#         if user_doc_number in directory_docs_list:
#             directory_docs_list.remove(user_doc_number)
#
#
#



# #по номеру документа выводит его имя
# def document_number_people():
#     num = input("Введите номер документа: ")
#     for document in documents:
#         if "number" in document.keys() and document["number"] == num:
#             print(document["name"])
#             break
#     else:
#         print("Документ не найден в базе")
#
#
# document_number_people()


# #по номеру документа выводит номер полки
# def get_shelf_number_by_doc():
#     doc_number = input('введите номер документа: ')
#     for enum in documents:
#         if doc_number != enum['number']:
#             print('такого документа нет в базe')
#         else:
#             if enum['number'] == doc_number:
#                 for enum_directories_key, enum_directories_value in directories.items():
#                     if doc_number in enum_directories_value:
#                       print('полка номер:', enum_directories_key)
# get_shelf_number_by_doc()


#добавит новую полку
# def add_new_shelf(directory=''):
#    new_shelf = input("Введите номер новой полки: ")
#    directories[new_shelf] = []
#    print(directories)
# add_new_shelf()

# def append_doc_to_shelf(user_doc_number, user_shelf_number):
#     add_new_shelf(user_shelf_number)
#     directories[user_shelf_number].append(user_doc_number)
#
## добавляет новый документ в каталог
# def add_new_user():
#     number = input('Введите номер документа: ')
#     doc_type = input('Введите тип документа: ')
#     name = input('Введите имя владельца документа: ')
#     directory = input('На какую полку положить? ')
#     new_doc = {"type":doc_type,"name":name, "number":number}
#     documents.append(new_doc)
#     append_doc_to_shelf(number,directory)
#     return directory
# add_new_user()
#
#
# #выводит список всех документов
# def document_list():
#     for document in documents:
#         for k,v in document.items():
#             print(f'{document["type"]},{document["number"]},{document["name"]}')
#             break
# document_list()

# #удаляет документ
# def deleting_user_by_document_number():
#     del_doc = input('Кого удаляем? Введите номер документа: ')
#     for document in documents:
#         if document["number"] == del_doc:
#             documents.remove(document)
#     else:
#         print('Такого документа нет')
#     print(documents)
# deleting_user_by_document_number()

#переместит документ на другую полку
# def moving_document_to_another_shelf():
#     user_doc_number = input('Введите номер документа, который нужно перенести: ')
#     user_shelf_number = input('Введите номер полки, на которую переносим документ: ')
#     doc_existence = False
#     if user_shelf_number not in directories:
#        print("Такой полки не существует")
#     for key,value in directories.items():
#         if user_doc_number in value:
#             doc_existence = True
#             directories[user_shelf_number] +=[user_doc_number]
#             value.remove(user_doc_number)
#     if doc_existence:
#         print("Документ успешно перемещён")
#     else:
#         print("Такого документа нет в базе")
#     print(directories)
# moving_document_to_another_shelf()

#main()

def get_name_by_number():
    number = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == number:
            print('{0}'.format(doc['name']))
            break
    else:
        print('Отсутствуют документы с таким номером')


def show_documents():
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])
    for key, values in directories.items():
        print(key, '->', values)


def get_directory_by_number():
    number = input('Введите номер документа: ')
    for directory, list_docs in directories.items():
        if number in list_docs:
            print('Документ с номером {0} находится на полке {1}'.format(number, directory))
            break
    else:
        print('Отсутствуют документы с таким номером')


def add_document():
    number = input('Введите номер документа:')
    name = input('Введите имя и фамилию:')
    doc_type = input('Введите тип документа:')
    directory_number = input('Введите номер полки:')
    if number and name and doc_type and directory_number:
        documents.append({"type": doc_type, "number": number, "name": name})
        if directory_number in directories:
            directories[directory_number].append(number)
        else:
            directories[directory_number] = [number]
    else:
        print('ВНИМАНИЕ! Введены не все данные')


def remove_document():
    person_number = input('Введите номер документа: ')
    bookshelf = ''
    for elem in documents:
        if elem['number'] == person_number:
            documents.remove(elem)
    for number_shelf, number_documents in directories.items():
        if person_number in number_documents:
            number_documents.remove(person_number)
            bookshelf = number_shelf
            break
    print(f'Удален документ с номером: {person_number} из базы данных и убран с полки №{bookshelf}')


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            get_name_by_number()
        elif command == 'l':
            show_documents()
        elif command == 's':
            get_directory_by_number()
        elif command == 'a':
            add_document()
        elif command == 'd':
            remove_document()
            print(documents)
            print(directories)
        elif command == 'e':
            break

main()







