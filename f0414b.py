# árvíztűrő tükörfúrógép ->
# arvizturo tukorfurogep

szoveg:str = input('írj be egy szöveget: ')
e:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
n:str = 'aeiooouuuAEIOOOUUU'

for k in szoveg:
    if k in e: szoveg = szoveg.replace(k, n[e.index(k)])

print(szoveg)