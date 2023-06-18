szelesseg=int(input('Hány méter széles a terület?: '))
hosszusag=int(input('Hány méter hossszú a terület?: '))
terulet=szelesseg*hosszusag
teruletNegysz=terulet*0.2780364289

print(f'A felszántandó terület:')
print(f'\tMérete (m2): {terulet}')
print(f'\tMérete (négyszögöl): {teruletNegysz}')
print(f'\tMunkadíj: {teruletNegysz*0.07+5000:.0f} Ft.')