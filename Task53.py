# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(например, имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

file_path = r'phone_base.txt'


def DataSearch(name):
    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            if name.casefold() in line.casefold():
                print(line)


def CreateContact(contact):
    with open(file_path, 'a', encoding='utf8') as f:        
        f.writelines('\n' + contact)
        print("Новый контакт добавлен")


# def change_file():
#     find_info = input()
#     new_info = input()
#     with open(file_path,'r+',encoding='UTF-8') as f:
#         for line in f:
#             if find_info.casefold() in line.casefold():
#                 if input("Да/Нет") == "Да":
#                     lst = (line.strip()).split(' ')
#                     print(lst)
#                 else: continue


print()
print("**********Добро пожаловать в наш телефонный справочник**********")
print()
while True:
    print()
    print("Пожалуйста выберите, что нужно сделать:")
    print()
    print("1. Найти контакт")    
    print("2. Создать новый контакт")
    print("3. Выйти из справочника")
    select_action = input("Ваш выбор: ")

    if select_action == "1":
        contact_name = input("Введите фамилию или имя контакта: ")
        DataSearch(contact_name)    
    elif select_action == "2":
        new_contact = input("Введите данные нового контакта: ")
        CreateContact(new_contact)
    elif select_action == "3":
        print("Всего доброго, заходите еще")
        break
    else:
        print("Неправильный ввод")