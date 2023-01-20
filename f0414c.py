szoveg:str = input('írj be egy szöveget: ')
e:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
n:str = 'aeiooouuuAEIOOOUUU'

for ek in e:
    szoveg = szoveg.replace(ek, n[e.index(ek)])

print(szoveg)