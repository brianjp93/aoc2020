CARD_PUB, DOOR_PUB = 8421034, 15993936
MOD = 20201227

def get_loop(pub_key, subject=7):
    start = subject
    loop = 0
    while start != pub_key:
        start = (start * subject) % MOD
        loop += 1
    return loop

card_loop, door_loop = get_loop(CARD_PUB), get_loop(DOOR_PUB)
enc = DOOR_PUB
for i in range(card_loop):
    enc = (enc * DOOR_PUB) % MOD

print(f'FINISH: {enc}')
