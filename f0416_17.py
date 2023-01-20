elso:str = input('írj be egy szót: ')
masodik:str = input('írj be egy másik szót: ')

e_kl:list[chr] = []
for k in elso:
    e_kl.append(k)

m_kl:list[chr] = []
for k in masodik:
    m_kl.append(k)

e_kl.sort()
m_kl.sort()

if e_kl == m_kl: print('anagramma')
else: print('nem anagramma')