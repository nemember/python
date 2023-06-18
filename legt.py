def mghSzama(szo):
    db=0
    for i in szo:
        if i in mgh:
            db+=1
    return db







napok=['hétfő','kedd','szerda','csütörtök','péntek']
mgh='aáeéiíuúüűoóöő'





maxPoz=0
for i in range(len(napok)):
    if mghSzama(napok[i])>mghSzama(napok[maxPoz]):
        maxPoz=i
    

print(f'A legtöbb magánhangzó a {napok[maxPoz]}-ben van. ')