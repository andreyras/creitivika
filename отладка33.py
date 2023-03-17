tasks = ['Понюхать пингвина', 'Испытать экзистенциальный ужас', 'Выключить утюг своих забот']

command = input('Введите команду: ')
while command != "выход":
    if command == "добавить":
        new_task = input("Добавить задачу: ")
        tasks.append(tasks, new_task)
        print('Добавлено!')
        print(tasks)
    else:
        print('Не знаю такой команды')
    command = input('Введите команду: ')
    