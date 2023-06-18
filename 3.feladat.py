class sofor:
    def __init__(self,sor:str):
        darabok=sor.strip().split(';')
        self.ora=int(darabok[0])
        self.perc=int(darabok[1])
        self.adasDb=int(darabok[2])
        self.nev=darabok[3]


sofi:list[sofor]=[]

f=open('cb.txt','r',encoding='UTF-8')
f.readline()
for sor in f:
    sofi.append((sor))
f.close()

print=len(sofi)