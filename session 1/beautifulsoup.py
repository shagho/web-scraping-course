from bs4 import BeautifulSoup
from pprint import pprint

html = '<ul class=country><li>Area<li>Population</ul>'
soup = BeautifulSoup(html, 'html5lib')

another_html = soup.prettify()
pprint(another_html)