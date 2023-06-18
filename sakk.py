class sakk:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.azonosito=int(adatok[0])
        self.nev=adatok[1]
        self.orszag=adatok[2]
        self.neme=adatok[3]
        self.eloPontszam=int(adatok[4])
        self.szulEv=adatok[5]



infok:list[sakk]=[]

f=open('sakk.txt','r',encoding='utf-8')
f.readline()
for sor in f:
    infok.append(sor)
f.close()


print(f'4. feladat: {len(infok)}')































































