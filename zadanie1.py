pers = {"имя":"сергей","свойство1":"сделал дз", "свойство2":"пошёл в школу","свойство3":"деградировать","суперспособность":"умеет существовать","особенности":"кудрявые волосы"}
print(pers)
key="ent"
while key !="off":
    key=input("vvedi: dob/ner/vix")
    if key == "dob":
        x=input("dobavte sv:")
        y=input("dobavte sv:")
        pers[y]=x
        if key == "ner":
            print(pers)
