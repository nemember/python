import random
import math
list=[]

for i in range(10):
    list.append(random.randint(10,99))



def ez_prím(szam):
    for item in list(2,int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True



print(list)
if ez_prím:
    print('Van prímszám a lsitában!')
else:
    print('Nincs prímszám a lsitában!')



























