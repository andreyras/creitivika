


pole = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', '*', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ]

x = 3
y = 4
dlpolya=len(pole)
for stroka in pole:
    for kvadr in stroka:
        print(kvadr, end = ' ')
    print()
command = input("Введи команду: ")
while command != "стоп":
    if command == "пр" and x<len(pole[0])-1:
        pole[y][x] = "O"
        x = x + 1
        pole[y][x] = "*"      
    elif command == "лв"and x<len(pole[0])-1:
        pole[y][x] = "O"
        x = x - 1
        pole[y][x] = "*"
    elif command == "в"and y<len(pole[0])-1:
        pole[y][x] = "O"
        y = y - 1
        pole[y][x] = "*"
    elif command == "нз"and y<len(pole[0])-1:
        pole[y][x] = "O"
        y = y + 1
        pole[y][x] = "*"
    else:
        print("Не понял...")
    for stroka in pole:
        for kvadr in stroka:
            print(kvadr, end = ' ')
        print()
    command = input("Введи команду: ")