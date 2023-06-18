suly=int(input('Kérem a súlyt kilogrammban: '))
magassag=int(input('Kérem a magasságot cm-ben: '))/100



def ttii():
    tti=suly/magassag**2
    return tti
index=ttii()

print(f'A testtömeg indexe: {index:.2f}')


if index<16:
        print(f'A testsúly osztálya: súlyos soványság')
elif 16<index<18.49:
        print(f'A testsúly osztálya: soványság')
elif 18.5<index<24.99:
        print(f'A testsúly osztálya: normális')    
elif 25<index<29.99:
        print(f'A testsúly osztálya: túlsúlyos')
elif index>30:
        print(f'A testsúly osztálya: elhízás')
    





