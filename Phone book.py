print("Телефонная книга")
print(""" Введите команду
1-Создать Контакт
2-Найти Контакт
3-Отредактировать Контакт
4-Удалить Контакт
5-Выйти""")
while True:
    print("Введите команду: ")
    command = input(' ')
    if command == '1':
        print ('Контакт добавлен')
    elif command == '2':
        print ('Контакт найден')
    elif command == '3':
        print ('Контакт отредактирован')
    elif command == '4':
        print ('Контакт удален')
    elif command == '5':
        import sys
        sys.exit()
    else:
        print("Неизвестная команда")