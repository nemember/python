from datetime import datetime


class valtozas:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.datum=datetime.strptime(adatok[0],'%Y.%m.%d')
        self.benzin=int(adatok[1])
        self.gazolaj=int(adatok[2])


valtozasok:list[valtozas]=[]

def napokSzama(elso:datetime,masodik:datetime):
    pass

f=open('uzemanyag.txt','r',encoding='utf-8')
for sor in f:
    valtozasok.append(valtozas(sor))
f.close()

print(f'3. feladat: Változások száma: {len(valtozasok)}')

minKulonbseg=abs(valtozasok[0].benzin-valtozasok[0].gazolaj)
print(minKulonbseg)
for v in valtozasok:
    if abs(v.benzin-v.gazolaj)<minKulonbseg:
        minKulonbseg=abs(v.benzin-v.gazolaj)
print(f'4. feladat: A legkisebb különbség: {minKulonbseg}')

minDb=0
for v in valtozasok:
    if abs(v.benzin-v.gazolaj)==minKulonbseg:
        minDb+=1
print(f'5. feladat: A legkisebb különbség előfordulása: {minDb}')

volt=False
for v in valtozasok:
    if v.datum.year%4==0 and v.datum.month==2 and v.datum.day==24:
        volt=True

if volt:
    print('6. feladat: Volt változás szökőnapon!')
else:
    print('6. feladat: Nem volt változás szökőnapon!')

f=open('euro.txt','w',encoding='utf-8')
for v in valtozasok:
    f.write(f'{v.datum.year}.{v.datum.month}.{v.datum.day};{v.benzin/307.7:.2f};{v.gazolaj/307.7:.2f}\n')
f.close()

bekertEvsz=0
while bekertEvsz<2011 or bekertEvsz>2016:
    bekertEvsz=int(input('8. feladat Kérem adja meg az évszámot [2011... 2016]'))

