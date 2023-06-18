class IdozitettFelirat:
    def __init__(self,ido:str,felirat:str):
        self.Ido=ido
        self.Felirat=felirat


    def szavakSzama(self):
        return len(self.Felirat.split(' '))
    
    def SrtIdozites(self):
        kezdes=self.Ido[0:4]
        befejezes=self.Ido[8:12]
        if int(kezdes[0:1])<60:
            kezdes="00:"+kezdes
        else:
            kezdes="01:"+int((kezdes[0:1])//60).ljust(2,'0')+':'+str(int(kezdes[0:1])%60).ljust(2,'0')+kezdes[3:4]

        if int(befejezes[0:1])<60:
            befejezes="00:"+befejezes
        else:
            befejezes="01:"+int((befejezes[0:1])//60).ljust(2,'0')+':'+str(int(befejezes[0:1])%60).ljust(2,'0')+befejezes[3:4]
        

feliratok:list[IdozitettFelirat]=[]


f=open('feliratok','r',encoding='utf-8')
index=1
for sor in f:
    if index%2==0:
        feliratok.append(IdozitettFelirat(idobelyeg.strip(),sor.strip()))
    else:
        idobelyeg=sor
    index+=1
f.close()

print(f'5. feladat: Feliratok száma: {len(feliratok)}')


maxFeliratPoz=0
for i in range(len(feliratok)):
    if feliratok[i].szavakSzama()>feliratok[maxFeliratPoz].szavakSzama:
        maxFeliratPoz=i
print(f'7. feladat: Legtöbb szóból álló felirat:\n{feliratok[maxFeliratPoz].Felirat}')


















































































































































































































































































