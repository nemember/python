import random


def névelő(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if szó[0].lower() in magánhangzók:
        return 'Az'
    return 'A'



def jelző():
    return random.choice(['piros','nagy','könnyed'])
    


print('Adj meg három főnevet! ')
for i in range(1,4):
    fonev=input(f'{str(i)}. főnév: ')
    print(f'{névelő(fonev)} {fonev} {jelző()}.')