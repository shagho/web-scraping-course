from lxml.html import fromstring, tostring
import requests

r = requests.get('https://fa.wikipedia.org/wiki/%D8%B1%D8%AF%D9%87:%D8%AF%D8%A7%D9%86%D8%B4%D9%85%D9%86%D8%AF%D8%A7%D9%86_%D8%B1%D8%A7%DB%8C%D8%A7%D9%86%D9%87')

tree = fromstring(r.text)

qwerty = tree.cssselect('#mw-pages > div > div > div > ul > li > a')

for item in qwerty:
    print(item.text_content())

