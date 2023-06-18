class nev:
    def __init__(self,sor:str):
        darabok=sor.strip().split(' ')
        self.Ev=int(darabok[0])
        self.Osztaly=(darabok[1])
        self.Nev=(darabok[2])

nevek:list[nev]=[]

f=open('nevek.txt','r',encoding='utf-8')
for sor in f:
    nevek.append((sor))
f.close()

print=len(nevek.Nev)

