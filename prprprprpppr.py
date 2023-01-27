import random
op=random.randint(0,9)
ok=random.randint(0,9)
of=random.randint(0,9)
def rand(op,ok,of):
    if op==ok:
        ok = ok + 1
        
    if ok>=100:
        -1
        
    if ok == of:
        of=of+1
    plus=str(op)+str(ok)+str(of)
    return plus

print(rand(op,ok,of))