def d(r):
    return x['rec']

players=[]
while True:
    d1=input('''add player, for examp:
    john
    15
    ''')
    x=input("")
    player={"name": d1, "rec" : x}
    players.append(player)
    players.sort(key=d)
    print(players)