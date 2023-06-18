class feltalalo:
    def __init__(self,sor:str):
        adatok=sor.strip().split('/')
        self.nev=adatok[0]
        self.szulEv=int(adatok[1])
        if adatok[2]=='':
            self.halEv=0
        else:
            self.halEv=int(adatok[2])
        self.talalmany=adatok[3]
        

feltalalok:list[feltalalo]=[0]
f=open('feltalalok.txt','r',encoding='utf-8')
for sor in f:
    feltalalok.append(feltalalo(sor))
f.close()

print(f'2. feladat: A fájlban {len(feltalalok)} tudós adata szerepel')

print(f'3. feladat: feltalálók-találmányok')


for item in feltalalok:
    print(f'{item.nev}=>{item.talalmany}')

kor=int(input('4. feladat: Kor megadása: '))
f=open('kiiras.txt', 'w',encoding='utf-8')
for item in feltalalok:
    if item.halEv-item.szulEv>kor:
        print({item.nev})
        f.write(f'{item.nev}\n')
f.close()
