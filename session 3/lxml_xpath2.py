from lxml.html import fromstring, tostring
import requests

r = requests.get('https://fa.wikipedia.org/wiki/%D8%B1%D8%AF%D9%87:%D8%AF%D8%A7%D9%86%D8%B4%D9%85%D9%86%D8%AF%D8%A7%D9%86_%D8%B1%D8%A7%DB%8C%D8%A7%D9%86%D9%87')
print(r.status_code)
tree = fromstring(r.text)

qwerty = tree.xpath('//div[@id="mw-pages"]/div[@class="mw-content-rtl"]/div[@class="mw-category mw-category-columns"]/div[@class="mw-category-group"]/ul/li/a/@href')

comp_content = []
for i in qwerty:
    r = requests.get('https://fa.wikipedia.org' + i)
    tree = fromstring(r.text)
    content = tree.xpath('//div[@class="mw-parser-output"]/p')
    for item in content:
        variable = ' '.join(item.xpath('text()'))
        if variable.strip() != "":
            comp_content.append((i, variable))
            break

print(comp_content)
print(len(comp_content))
