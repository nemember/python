class jelolt:
    def __init__(self,sor:str):
        adatok=sor.strip().split(' ')
        self.kerulet=int(adatok[0])
        self.szavazatok=int(adatok[1])
        self.nev=adatok[2]+' '+adatok[3]
        self.part=adatok[4]


jeloltek:list[jelolt]=[]

f=open('szavazatok.txt','r',encoding='utf-8')
for sor in f:
    jeloltek.append(jelolt(sor))
f.close()


print(f'2. feladat: A választáson {len(jeloltek)} képviselőjelölt indult.')

bekertNev=input('3. feladat: Képviselő neve: ')
talalt=False #még nincs találat
for item in jeloltek:
    if item.nev==bekertNev:
        talalt=True
        print(f'\tA jelölt a {item.kerulet}-s számú körzetben indult.')
        print(f'\tA kapott szavazatok száma: {item.szavazatok}')
if talalt==False:
    print(f'\tIlyen nevű képviselőjelölt nem szerelepkoskjbebvj')


szavazok=0
for item in jeloltek:
    szavazok+=item.szavazatok
print(f'4. feladat: A választáson {szavazok} szavazó a jogosultak {(szavazok/12345*100):.2f}%-a vett részt')

maxPoz=0 
for i in range(len(jeloltek)):
    if jeloltek[i].szavazatok>jeloltek[maxPoz].szavazatok:
        maxPoz=i

print(f'5. feladat: A legtöbb szavazat:')
print(f'\t{jeloltek[maxPoz].nev} - ',end='')
if jeloltek[maxPoz].part=='-':
    print(f'független: {jeloltek[maxPoz].part}  szavazat')
else:
    print(f'független: {jeloltek[maxPoz].part}: {jeloltek[maxPoz].szavazatok} szavazat')


stat={}
for item in jeloltek:
    if item.part in stat.keys():
        stat[item.part]+=item.szavazatok
    else:
        stat[item.part]=item.szavazatok

print(f'6. feladat')
for key,value in stat.items():
    if key=='-':
        key='Független'
    print(f'\t{key}: {value} szavazat')


f=open('TISZ.csv','w',encoding='utf-8')
f.write('Körzet;Név;Szavazatok száma\n')
for item in jeloltek:
    if item.part=='TISZ':
        f.write(f'{item.kerulet};{item.nev};{item.szavazatok}\n')
f.close()






























































































































































































































































































































































































































































































a=0