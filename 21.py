import random
a=random.randint(1,8)
m=int(input())
while m!=a:
    if m >a:
        print("Бери меньше")
        m=int(input())
    elif m <a:
        print("Бери больше")
        m=int(input())
else:
    print("на лаки")

  

    