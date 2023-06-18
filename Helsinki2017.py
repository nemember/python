class helsinki:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.Nev=adatok[0]
        self.Orszag=adatok[1]
        self.Technikai=float(adatok[2])
        self.Komponens=float(adatok[3])
        self.Levonás=int(adatok[4])



donto:list[helsinki]=[]
rovid:list[helsinki]=[]

f=open('donto.csv','r',encoding='utf-8')
f.readline()
for sor in f:
    donto.append(helsinki(sor))
f.close()

a=open('rovidprogram.csv','r',encoding='utf-8')
a.readline()
for sor in a:
    rovid.append(helsinki(sor))
a.close()

print(f'2. feladat: \n\tA rövidprogramban {len(rovid)} induló volt')


igaz=False
for self in donto:
    if self.Orszag=='HUN':
        igaz=True

if igaz==True:
    print(f'3. feladat: \n\tA magyar versenyző bejutott a kűrbe')
else:
    print(f'3. feladat: \n\tA magyar versenyző nem jutott be a kűrbe')


bekNev=input('5. feladat: \n\tKérem a versenyző nevét: ')
def Összpontszám(pontszam):
    for item in rovid:
        if item.Nev == bekNev:
            pontszam+=item.Technikai
            pontszam+=item.Komponens
            pontszam=item.Levonás
            break

    for item in donto:
        if item.Nev == bekNev:
            pontszam+=item.Technikai
            pontszam+=item.Komponens
            pontszam=item.Levonás
            break

    return(pontszam)






























































































































