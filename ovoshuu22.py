print("vvedi komandy pzhhhhh")
print("komandi: add, delindex, vs")
komandi=["cdelat dz, cxodit v magaz, ubratsya v komnate, poest"]
com=input("komanda: ")
if com == "add":
    a=input("vpishi chto-to:")
    komandi.append(a)
    print(komandi)
elif com == "delindex":
    a=int(input("pishi index:"))
    del komandi[a]
    print(komandi)
elif com =="vs" :
    print(komandi)
     