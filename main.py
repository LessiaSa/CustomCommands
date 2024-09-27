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

#проверка существования документа
def check_document_number(user_doc_number):
    doc_founded = False
    for document in documents:
        doc_number = document["number"]  #завожу переменную для хранения существующего номера документа
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded

#проверка существования полки
def check_shelf_number(user_shelf_number):
    shelf_founded = False
    for directory in directories:
        shelf_number = directory[0]
        if shelf_number == user_shelf_number:
            shelf_founded = True
            break
    return shelf_founded

#удалить документ с полки
def remove_doc_from_shelf(user_doc_number):
    for directory_number, directory_docs_list in directories.items():
        if user_doc_number in directory_docs_list:
            directory_docs_list.remove(user_doc_number)






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









