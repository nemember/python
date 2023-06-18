def fordit(mondat:str):
    szavak=mondat.split(' ')
    ujMondat=''
    for szo in szavak:
        ujSzo=szo[::-1]
        ujMondat+=ujSzo+' '
    return ujMondat





bekertMondat=''
while(bekertMondat!='VÉGE'):
    bekertMondat=input('Kérek egy szöveget: ')
    if bekertMondat!='VÉGE':
        print(f'A szöveg visszafele: {fordit(bekertMondat)}')