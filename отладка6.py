'''
Суммадий решил переписать калькулятор с использованием подпрограмм.
Он создал функцию суммирования, вставил её в код калькулятора...
Но результат не выводится. Как исправить это?
'''
summa=0
def summ():
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите второе число: '))
    print(num1+num2)
    return num1+num2

command = input('Введите команду: ')
while command!="выход":
    if command == "+":
        summ()
    elif command == "-":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1-num2)
    elif command == "*":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1*num2)
    elif command == "/":
        num1 = int(input('Введите число: '))
        num2 = int(input('Введите второе число: '))
        print(num1/num2)
    command = input('Введите команду: ')
print("Калькулятор выключен")