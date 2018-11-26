from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.multipasko.pl/wyniki-lotto/multi-lotek/'

r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser')

mm = soup.find('div', id='ostatnie_mm')
li = mm.find_all('li')
h4 = mm.find('h4').get_text()
lplus = mm.find('li', class_='plus').get_text()



lista = []

for l in li:
    l1 = l.get_text()
    lista.append(l1)
    # print(l1.split(), end='')

listaInt = [int(i) for i in lista] # zamieniam listę string na int


print("""
""")
print(h4)
print("""
""")
print(' '.join(lista), end='')
print(' plus: '+lplus)
print()

# funkcja w której podajemy liczby do sprawdzenia np z kuponu
def loopek():
    print()
    print('Podaj liczby po spacji (bez przecinków) które chcesz sprawdzić : ')
    print()
    liczby = input()
    
    # spr czy w inpucie są litery, lub pusty string, jeśli tak konczy program
    if liczby.isalpha() or liczby == '':
        print("""
        Podałeś nie poprawne znaki, koniec programu!
        """)
        sys.exit()
    else:
        wyniki = [int(x) for x in liczby.split()]
        wyniki.sort()

    print()
    print('Sprawdzam trafione liczby : ', end='')
    print(len(sorted(set(listaInt) & set(wyniki))))
    print(sorted(set(listaInt) & set(wyniki)))
    print()

loopek()

# pętla z pytaniem czy chcesz jeszcze raz podać inne numery
def loop2():
    print('Chcesz sprawdzić więcej kuponów? : T lub N')
    odp = input()
    if odp == 't' or odp == 'T':
        loopek()
    elif odp == 'n' or odp == 'N': 
        sys.exit()
        
while True:
    loop2()
    if False:
        break
    



