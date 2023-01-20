# árvíztűrő tükörfúrógép ->
# arvizturo tukorfurogep

szoveg:str = input('írj be egy szöveget: ')
e:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
n:str = 'aeiooouuuAEIOOOUUU'
ekezet_mentes = ''
for k in szoveg:
    if k in e: ekezet_mentes += n[e.index(k)]
    else: ekezet_mentes += k
print(f'szöveg ékezetek nélkül: {ekezet_mentes}')

