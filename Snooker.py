class snooker:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.helyezes=int(adatok[0])
        self.nev=(adatok[1])
        self.orszag=adatok[2]
        self.nyeremeny=int(adatok[3])


snookerek:list[snooker]=[]

f=open('snooker.txt','r',encoding='utf-8')
f.readline()
for sor in f:
    snookerek.append(snooker(sor))
f.close()

print(f'3. feladat: A vilgranglistán {len(snookerek)} versenyző szerepel')


def atlag():
    penz=0
    for item in snookerek:
        penz+=item.nyeremeny
    return penz/len(snookerek)


print(f'4. feladat: A versenyzők átlagosan {atlag():.2f} fontot kerestek')




#def topMoney():
    