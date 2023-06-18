elso=(input('Adj meg egy szót! '))
masodik=(input('Adj meg egy másik szót! '))

if len(elso) > len(masodik):
    print(f'A hosszabb szó {elso}')
elif len(masodik)>len(elso):
    print(f'A hosszabb szó {masodik}')
else:
    print('A két szó geyenló hosszú.')