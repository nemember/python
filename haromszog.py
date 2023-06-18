print('1. feladat: A háromszög szerkeszthetősége')
print('Kérem a háromszög oldalait')



a=float(input('a ='))
b=float(input('b ='))
c=float(input('c ='))



if a<b+c and b<a+c and c<a+b:
    print('A háromszög megszerkeszthető!')
else:
    print('A háromszög nem szerkeszthető a megadott adatokkal!')

