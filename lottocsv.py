from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.multipasko.pl/wyniki-lotto/multi-lotek/'

r = requests.get(url).text

zupa = BeautifulSoup(r, 'html.parser')

mm = zupa.find('div', id='ostatnie_mm')
li = mm.find_all('li')
h4 = mm.find('h4').get_text()
nrPlus = mm.find('li', class_='plus').get_text()

lista = []

for l in li:
    l1 = l.get_text()
    lista.append(l1)
    # print(l1.split(), end='')

listaInt = [int(i) for i in lista] # zamienia listę string na int
nowaLista = ', '.join(map(str, listaInt)) # usuwa nawiasy [ ] z listy

# zapis do pliku z datą pobieraną ze strony url oraz resztą danych
with open(h4.replace(':', '-') +'.txt', 'w') as f:
    f.write(nowaLista +'\n')
    f.write('Plus : ' + nrPlus)




# DO CSV
# with open(h4.replace(':', '-') +'.txt', 'w', newline='') as f:
#     writercsv = csv.writer(f)
#     writercsv.writerow(nowaLista)
#     writercsv.writerow(nrPlus)

