from datetime import datetime

class Fuvar:
    def __init__(self,sor:str):
        darabok=sor.strip().split(';')
        self.azonosito=int(darabok[0])
        self.indulas=datetime.strptime(darabok[1], '%Y-%m-%d %H:%M:%S')
        self.ido=int(darabok[2])
        self.tavolsag=float(darabok[3].replace(',','.'))
        self.viteldij=float(darabok[4].replace(',','.'))
        self.borravalo=float(darabok[5].replace(',','.'))
        self.fizetes=darabok[6]

fuvarok:list[Fuvar]=[]

f=open('fuvar.csv','r',encoding='utf-8')
elsoSor=f.readline().strip()
for sor in f:
    fuvarok.append(Fuvar(sor))
f.close()

print(f'3. feladat: {len(fuvarok)} fuvar')

fuvarDb=0
penz=0
for fuvar in fuvarok:
    if fuvar.azonosito==6185:
        fuvarDb+=1
        penz+=fuvar.viteldij
print(f'4. feladat: {fuvarDb} fuvar alatt: {f"{penz}".replace(".",",")}$')


fizetesiMod={}
for fuvar in fuvarok:
    if fuvar.fizetes in fizetesiMod.keys():
        fizetesiMod[fuvar.fizetes]+=1
    else:
        fizetesiMod[fuvar.fizetes]=1

print('5. feladat:')
for key,value in fizetesiMod.items():
    print(f'\t{key}: {value} fuvar')


osszTav=0
for fuvar in fuvarok:
    osszTav+=fuvar.tavolsag
print(f'6. feladat: {f"{osszTav*1.6:.2f}".replace(".",",")}km')


maxIdoPoz=0
for i in range(len(fuvarok)):
    if fuvarok[i].ido > fuvarok[maxIdoPoz].ido:
        maxIdoPoz=i

print('7. feladat: Leghosszabb fuvar')
print(f'\tFuvar hossza: {fuvarok[maxIdoPoz].ido} másodperc')
print(f'\tTaxi azonosító: {fuvarok[maxIdoPoz].azonosito}')
print(f'\tMegtett távolság: {f"{fuvarok[maxIdoPoz].tavolsag}".replace(".",",")} mérföld')
print(f'\tViteldíj: {f"{fuvarok[maxIdoPoz].viteldij}".replace(".",",")}$')
























































































        
    
















































        