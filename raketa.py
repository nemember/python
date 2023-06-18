visszaSzamlalas=int(input('Hány órás visszaszámlálást tervezünk?' ))
felfuggesztes=0

for i in range(visszaSzamlalas,0,-1):
    print(f'Visszaszámlálás: {i}')
    valasz=input('Fel kell függeszteni a visszaszámlálást (i/n) ')
    if valasz=='i':
        felfuggesztes+=1

print(f'A rakéta a visszaszámlálást követően ennyi órával indult: {visszaSzamlalas+felfuggesztes}')