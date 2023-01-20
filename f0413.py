maganhangzok:str = 'aáeéiíoóöőuúüű'

szo:str = input('írj be egy szót: ').lower()

msz:int = 0
for k in szo:
    if k in maganhangzok: msz += 1
print(f'a magánhangzók száma a szövegben: {msz}')