from lxml.html import fromstring, tostring
html = '<ul class=country><li>Area<li>Population</ul>'
tree = fromstring(html)
another_html = tostring(tree, pretty_print=True)

print(another_html)