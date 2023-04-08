from bs4 import BeautifulSoup
from pprint import pprint

html = '<ul class=country><li>Area<li>Population</ul>'
soup = BeautifulSoup(html, 'html5lib')

ul = soup.find('ul', attrs={'class': 'country'})
print('first match:\n')
print(ul.find('li'))
print('all matches:\n')
print(ul.find_all('li'))