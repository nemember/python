def tokeletes(szam):
    osztoOsszeg=0
    for i in range(1,szam//2+1):
        if szam%i==0:
            osztoOsszeg+=i
    if szam==osztoOsszeg:
        return True
    return False



print ('2. feladat: Tökéletes számok\nKérek két természetes számot:')
tol=int(input('tól = '))
ig=int(input('ig = '))

print(f'Tökéletes számok {tol} és {ig} között:')
db=0
for i in range(tol,ig+1):
    if tokeletes(i):
        db+=1
        if db==1:
            print(f'{i}',end='')
        else:
            print(f'; {i}',end='')
    
if db==0:
    print('A megadott tartományban nincsen tökéletes szám!')