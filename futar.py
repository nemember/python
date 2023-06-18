class Fuvar:
    def __init__(self,sor:str):
        adatok=sor.strip().split(' ')
        self.nap=int(adatok[0])
        self.sorszam=int(adatok[1])
        self.tav=int(adatok[2])



fuvarok:list[Fuvar]=[]


f=open('tavok.txt','r',encoding='utf-8')
for sor in f:
    fuvarok.append(Fuvar(sor))
f.close()


minNap=fuvarok[0].nap
for item in fuvarok:
    if item.nap < minNap:
        minNap=item.nap
if item.nap==minNap and item.sorszam==1:
    elsoFuvar=item.tav



print(f'2. Feladat:\n\tAz első fuvar hossza: {elsoFuvar} km')

maxNap=fuvarok[0].nap
for item in fuvarok:
    if item.nap > minNap:
        minNap=item.nap

maxnaomaxsorszam=fuvarok[0].sorszam
for item in fuvarok:
    if item.nap==maxNap and item.sorszam>maxnaomaxsorszam:
        maxnaomaxsorszam=item.sorszam

for item in fuvarok:
    if item.nap==maxNap and item.sorszam==maxnaomaxsorszam:
        utolsoFuvar=item.tav

print(f'3. feladat:\n\tAz utolsó fuvar hossza: {utolsoFuvar} km')

napok=set()
for item in fuvarok:
    napok.add(item)
print(f'4.feldaldlat:{napok}')
for i in range(1,8):
    if i not in napok:
        print(f'\t{i}. nap')

maxFuvarDbPoz=0
for i in range(len(fuvarok)):
    if fuvarok[i].sorszam>fuvarok[maxFuvarDbPoz]:
        maxFuvarDbPoz=i

print(f'5. feladat:\n\tA legtöbb fuvar a hét {fuvarok[maxFuvarDbPoz]}. napján volt, összesen {fuvarok[maxFuvarDbPoz].sorszam} db.')


stat={}
for i in range(1,8):
    stat[i]=0
for fuvar in fuvarok:
    stat[fuvar.nap]+=fuvar.tav

print('6. feladat: Az egyes napokon tekert kilométerek:')
for key, value in stat.items():
    print(f'\t{key}. nap: {value} km')



bekertTav=int(input('7. Feladat: Adjon meg egy távolságot: '))






























































