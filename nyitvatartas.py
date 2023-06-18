most=int(input('Hány óra van most? '))

if most>=8 and most < 16:
    print('A bolt nyitva van.')
    print(f'Ennyi órád van még odaérni: {16-most}')
else:
    print('A bolt zárva van')