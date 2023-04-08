from lxml.html import fromstring, tostring
html = '<ul class=country><li id=werty>Area<li id=132>Population</ul>'
tree = fromstring(html)
print(tree.xpath('//ul[@class="country"]/li[@id="werty"]/text()')[0])