class batalon:
    def __init__(self,sor:str):
        adatok=sor.strip().split(' ')
        self.adoszam=int(adatok[0])
        self.utca=adatok[1]
        self.házszám=adatok[2]
        self.adósáv=adatok[3]
        self.alapt=int(adatok[4])


Balaton:list[batalon]=[]

f=open('utca.txt','r',encoding='utf-8')
f.readline()
for sor in f:
    Balaton.append(batalon(sor))
f.close()


db=0
for i in Balaton:
    db+=1

print(f'2. feladat: {db} db')


idk= int(input('Adószáááám ?'))
for i in Balaton:
    if idk==i.adoszam:
        print(f'3. feladat: {i.utca} {i.házszám}')


