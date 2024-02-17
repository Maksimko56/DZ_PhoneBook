tem_book = [] #Глобальная переменная, временное хранение книги


# Открытие книги
def open_book():
    global tem_book
    try:
        book = open("phone_book.txt", "r", encoding="utf-8")
    except IOError as e:
        book = open("phone_book.txt", "w", encoding="utf-8")
    else:
        with book:
            tem_book = list(book)
    book.close()

# # Создать контакт
def add_contact():
    global tem_book
    fio = input("Введите имя: ")
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    tem_book.append(f"{fio},{number},{comment}\n")
    return True


# Показть все контакты
def all_contacts():
    global tem_book
    return tem_book


# Найти контакт
def find_contact():
    tem_book = all_contacts()
    count = 0
    if (what := input("Что будем искать?\n(Выбирите 1-фио, 2-номер, 3-комментарий)?: ")) == "1": # Поиск по имени
        fio = input("Введите имя: ").lower()
        for contact in tem_book:
            if fio in contact.lower().split(",")[0]:
                count += 1
                print(contact,end='')
        if count == 0:
            print("Такого нет!")
            find_contact()

    elif what == "2": # Поиск по номеру
        number = input("Введите номер: ").lower()
        for contact in tem_book:
            if number in contact.lower().split(",")[1]:
                count += 1
                print(contact,end='')
        if count == 0:
             print("Такого нет!")
             find_contact()

    elif what == "3":   # Поиск по коментариям
        comment = input("Введите комментарий: ").lower()
        for contact in tem_book:
            if comment in contact.lower().split(",")[2]:
                count += 1
                print(contact, end='')
        if count == 0:
            print("Такого нет!")
            find_contact()
    else:
        print("Повторите выбор!")
        find_contact()

# Изменить контакт
def edit_contact():
    tem_book = all_contacts()
    count =0
    if (what := input("Что будем менять?\n(Выбирите 1-фио, 2-номер, 3-комментарий)?: ")) == "1":
        fio = input("Кого будем менять: ").lower()
        for id,contact in enumerate(tem_book):
            if fio in contact.lower().split(",")[0]:
                print(id,contact, end='')
                count+=1
        if count > 0:
            change_name_id = int(input('введите № id кого меняем?: '))
            new_name = input('Введите новое имя для контакта: ')
            tem_book[change_name_id] = f"{new_name},{tem_book[change_name_id].split(',')[1]},{tem_book[change_name_id].split(',')[2]}"
            return True
        else:
            print("Такого нет")
            edit_contact()
    elif what == "2":
        number = input("Введите номер: ").lower()
        for id,contact in enumerate(tem_book):
            if number in contact.lower().split(",")[1]:
                print(id,contact, end='')
                count +=1
        if count > 0:
            change_name_id = int(input('введите № id кого меняем?: '))
            new_number = input('Введите новый номер: ')
            tem_book[change_name_id] = f"{tem_book[change_name_id].split(',')[0]},{new_number},{tem_book[change_name_id].split(',')[2]}"
            return True
        else:
            print("Такого нет")
            edit_contact()
    elif what == "3":
        comment = input("Введите комментарий: ").lower()
        for id, contact in enumerate(tem_book):
            if comment in contact.lower().split(",")[2]:
                print(id,contact, end='')
                count += 1
        if count > 0:
            change_name_id = int(input('введите № id кого меняем?: '))
            new_coment = input('Введите новый коментарий: ')
            tem_book[change_name_id] = f"{tem_book[change_name_id].split(',')[0]},{tem_book[change_name_id].split(',')[1]},{new_coment}\n"
            return True
        else:
            print("Такого нет")
            edit_contact()
    else:
        print("Повторите выбор!")
        edit_contact()



def del_contacts():
    count =0
    tem_book = all_contacts()
    fio = input("Введите имя удаляемого контакта: ").lower()
    for id, contact in enumerate(tem_book):
        if fio in contact.lower().split(",")[0]:
                print(id,contact)
                count += 1
    if count > 0:
            change_name_id = int(input('введите № id кого удаляемого?: '))
            del tem_book[change_name_id]
            return True
    else:
            print("Повторите выбор!")
            del_contacts()


def save_book():
    tem_book = all_contacts()
    file = open("phone_book.txt", "w", encoding="utf-8")
    for contact in tem_book:
        wr = f"{contact.split(',')[0]},{contact.split(',')[1]},{contact.split(',')[2]}"
        file.write(str(wr))
    file.close()

def phone_books():
    open_try = False
    edit_try = ''
    global tem_book

    while True:
        print("\n1. Открыть справочник\n"
              "2. Сохраниить  справончик\n"
              "3. Показть все контакты\n"
              "4. Создать контакт\n"
              "5. Найти контакт\n"
              "6. Изменить контакт\n"
              "7. Удалить контакт\n"
              "8. Выход\n")
        if (numb:=input("Выбирете действие из списка: \n")) == "1":
            open_book()
            print("Справочник открыт")
            open_try = True
        elif numb == "2":
            if open_try:
                 save_book()
                 edit_try = False
            else:
                print("Справочник не открыт!")
        elif numb == "3":
            if open_try:
                print(*all_contacts())
            else:
                print("Справочник не открыт!")
        elif numb == "4":
            if open_try:
                edit_try = add_contact()
            else:
                print("Справочник не открыт!")

        elif numb == "5":
            if open_try:
                find_contact()
            else:
                print("Справочник не открыт!")
        elif numb == "6":
            if open_try:
                edit_try = edit_contact()
            else:
                print("Справочник не открыт!")
        elif numb == "7":
            if open_try:
                edit_try = del_contacts()
            else:
                print("Справочник не открыт!")
        elif numb == "8":
                if edit_try:
                    print("У вас есть не сохраненные изменения!")
                    if input("Сохранить их? y/n: ") == "y":
                        save_book()
                        break
                break

phone_books()