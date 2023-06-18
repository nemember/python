class versenyzo:
    def __init__(self,sor:str):
        darabok=sor.strip().split(';')
        self.nev=darabok[0]
        self.szuldat=darabok[1]
        self.nemzetiseg=darabok[2]
        self.rajtszam=darabok[3]



versenyzok:list[versenyzo]=[]
def beolvas():
    f=open('pilotak.csv','r',encoding='utf-8')
    f.readline()
    for sor in f:
        versenyzok.append(versenyzo(sor))
    f.close()
beolvas()


print(f'3. feladat: {len(versenyzok)}')

print(f'4. feladat: {versenyzok[-1].nev}')

print('5.feladat:')
for vers in versenyzok:
    if int(vers.szuldat[:4])<1901:
        print(f'\t{vers.nev} ({vers.szuldat})')


minRszPoz=0
for i in range(len(versenyzok)):
    if versenyzok[i].rajtszam!='':
        if int(versenyzok[i].rajtszam)<int(versenyzok[minRszPoz].rajtszam):
            minRszPoz=i


print(f'6. feladat: {versenyzok[minRszPoz].nemzetiseg}')

rajtszamok={}
for vers in versenyzok:
    if vers.rajtszam!='':
        if vers.rajtszam in rajtszamok.keys():
            rajtszamok[vers.rajtszam]+=1
        else:
            rajtszamok[vers.rajtszam]=1

print('7. feladat: ',end='')
db=0
for key, value in rajtszamok.items():
    if value>1:
        if db==0:
            print(f'{key}',end='')
        else:
            print(f', {key}',end='')
        db+=1
































































































































