import mylib

mylib.vyvodPolya(mylib.vidimost_polya)
game = True
bombs=5
while game:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    if stroka >12 or stolb >12:
        break
    if stroka=="$" and stolb=="$":
        break
    # передадим не номера строки и столбца, а индексы
    mylib.check(stroka-1,stolb-1)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
            game = False
            
print("Всё поле открыто!")












