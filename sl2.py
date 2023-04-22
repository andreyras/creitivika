perc={'ФИО':'Василий Никитин Романович','русский язык':3,'геометрия,алгебра':4,'физика':4}
perc1={'ФИО':'Алексей Анашкин Николаевич','русский язык':5,'геометрия,алгебра':4,'физика':4}
perc2={'ФИО':'Александр Кутовых Евгеньевич','русский язык':4,'геометрия,алгебра':5,'физика':3}
print(perc, perc1, perc2)
key='ent'
while key !="off":
    key=input("vvedi: dob/ner/vix")
    if key == "dob":
        y=input("dobavte predm :")
        x=input("dobavte ocenky :")
        perc[y]=x
    if key == "ner":
        while True:
            predmet = input("izmenite predmet oc dlya kotorogo xotite izmenit :")
            oc = input("izmenite oc predmet dlya kotoroi zotite izmenit :")
            if predmet in perc.keys():
                perc[predmet]=oc
            else:
                print("takogo predmeta net")
    if key=="vix":
        print(perc)
