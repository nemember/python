class EU:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.orszag=adatok[0]
        self.csat=adatok[1]


Orszagok:list[EU]=[]

f=open('EUcsatlakozas.txt','r',encoding='utf-8')
for sor in f:
    Orszagok.append(EU(sor))
f.close()

print(f'3. feladat: EU tagállamainak száma: {len(Orszagok)}db')


db=0
for i in Orszagok:
    if int(i.csat[0:4])==2007:
        db+=1
        

print(f'2007-ben {db} ország csatlakozott')
    


for i in Orszagok:
    if i.orszag=='Magyarország':
        print(f'5. feladatMagyarország csatlakozásának dátuma: {i.csat}')


for i in Orszagok:
    if int(i.csat[6]) == 5:
        print(f'Májusban volt csatlakozás!')
        break
    else:
        print(f'Májusban nem volt csatlakozás!')

    
    

