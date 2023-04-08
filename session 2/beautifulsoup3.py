import requests
from bs4 import BeautifulSoup

r = requests.get('https://fa.wikipedia.org/wiki/%D8%B1%D8%AF%D9%87:%D8%AF%D8%A7%D9%86%D8%B4%D9%85%D9%86%D8%AF%D8%A7%D9%86_%D8%B1%D8%A7%DB%8C%D8%A7%D9%86%D9%87')
soup = BeautifulSoup(r.text, 'html5lib')

empty_list = []

divs = soup.find_all('div', attrs={'class': 'mw-category-group'})
for item in divs:
    for i in item.find_all('a'):
        empty_list.append(i.text)

print(empty_list)
