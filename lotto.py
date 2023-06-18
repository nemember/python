class sorsolas:
    def __init__(self,sor:str):
        adatok=sor.strip().split(' ')
        self.hetiSzamok=[]
        for szam in adatok:
            self.hetiSzamok.append(szam)

sorsolasok:list[sorsolas]=[]

bekert=sorsolas(input('1. feladat: Adja meg az 52. heti számokat: '))
print(f'\tNövekvő sorrendben: ',end='')
bekert.hetiSzamok.sort()
for szam in bekert.hetiSzamok:
    print(f'{szam}',end=' ')


f=open('lottosz.txt','r',encoding='utf-8')
for sor in f:
    sorsolasok.append(sorsolas(sor))
f.close()

szam=int(input('\n3.feladat: Kérem adja meg a hét számát (1-51): '))
print('\tNyerőszámok: ',end='')
for szam in sorsolasok[szam-1].hetiSzamok:
    print(f'{szam} ',end='')
#print(f'\tNYerőszámok: {" ".join(str(e) for e in sorsolasok[szam-1].hetiSzamok)}')

db=0
for i in range(1,91):
    van=False
    for egyHet in sorsolasok:
        if i in egyHet.hetiSzamok:
            van=True


eddigKihuzott=set()
for item in sorsolasok:
    for szam in item.hetiSzamok:
        eddigKihuzott.add(szam)
if len(eddigKihuzott)!=90:
    print(f'\n5. feladat: Van olyan szám, amit nem húztak ki.')
else:
    print(f'\n5. feladat: Nincs olyan szám, amit nem húztak ki.')

paratlanDb=0
for egyHet in sorsolasok:
    for szam in egyHet.hetiSzamok:
        if szam%2==1:
            paratlanDb+=1
print(f'6. feladat: {paratlanDb} alkalommal húztak ki páratlan számot.')


sorsolasok.append(bekert)
f=open('lotto52.txt','w',encoding='utf-8')
for egyHet in sorsolasok:
    f.write(f'{" ".join(str(e) for e in sorsolasok[szam-1].hetiSzamok)}')
f.close()





















































































































































































































































































































































