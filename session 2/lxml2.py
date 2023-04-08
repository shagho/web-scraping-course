from lxml.html import fromstring, tostring
html = '<ul class=country><li id=werty>Area<li id=132>Population</ul>'
tree = fromstring(html)

ul = tree.cssselect('ul.country > li#132')
print(ul[0].text_content())