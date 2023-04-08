# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

import os

file_path = r'phone_base.txt'
new_file = r'fileTMP.txt'


def DataSearch():
    name = input("Введите фамилию или имя контакта: ")

    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            if name.casefold() in line.casefold():
                return(line)


def CreateContact(contact):
    with open(file_path, 'a', encoding='utf8') as f:        
        f.writelines('\n' + contact)
        


def ChangeContact():    
    name = input("Введите данные контакта: ")

    with open(file_path, 'r', encoding='utf8') as oldfile, open(new_file, "w", encoding='utf8') as newfile:    
        for line in oldfile:
            if name.casefold() in line.casefold():
                print(line)
                choose = input("Этот контакт будем исправлять? (1 - да, 2 - нет): ")
                if choose == "1":
                    changes = input("Введите исправленную информацию: ")
                    newfile.write(changes)
                elif choose == "2":
                    print("Ищем дальше")
                    newfile.write(line)
                else:
                    print("Неправильный ввод")
            else:
                newfile.write(line)
    os.remove(file_path)
    os.rename(new_file, file_path)


def DeleteContact():    
    name = input("Введите данные контакта: ")

    with open(file_path, 'r', encoding='utf8') as oldfile, open(new_file, "w", encoding='utf8') as newfile:    
        for line in oldfile:
            if name.casefold() in line.casefold():
                print(line)
                choose = input("Этот контакт будем удалять? (1 - да, 2 - нет): ")
                if choose == "1":
                    print("Контакт удалён")                    
                elif choose == "2":
                    print("Ищем дальше")
                    newfile.write(line)
                else:
                    print("Неправильный ввод")
            else:
                newfile.write(line)
    os.remove(file_path)
    os.rename(new_file, file_path)
        

print()
print("**********Добро пожаловать в наш телефонный справочник**********")
print()
while True:
    print()
    print("Пожалуйста выберите, что нужно сделать:")
    print()
    print("1. Найти контакт")    
    print("2. Создать новый контакт")
    print("3. Внести изменения")
    print("4. Удалить контакт")
    print("5. Выйти из справочника")
    select_action = input("Ваш выбор: ")

    if select_action == "1":        
        print(DataSearch())    
    elif select_action == "2":        
        contact = input("Введите данные нового контакта: ")
        CreateContact(contact)
        print("Новый контакт добавлен")
    elif select_action == "3":        
        ChangeContact()
    elif select_action == "4":        
        DeleteContact()
    elif select_action == "5":
        print("Всего доброго, заходите еще")
        break
    else:
        print("Неправильный ввод")