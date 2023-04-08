import requests
import re

r = requests.get("https://fa.wikipedia.org/wiki/%D8%B1%D8%AF%D9%87:%D8%AF%D8%A7%D9%86%D8%B4%D9%85%D9%86%D8%AF%D8%A7%D9%86_%D8%B1%D8%A7%DB%8C%D8%A7%D9%86%D9%87")

ert = re.findall(r'<div class="mw-category-group">((.|\n)*?)</div>', r.text)
qwert = []
for item in ert:
    temp = re.findall(r'<li>((\n|.)*?)</li>', item[0])
    if temp:
        for i in temp:
            qwert.append(i)

for item in qwert:
    print(re.findall(r'<a href=\"(.*?)\" title=\"(.*?)\">(.*?)\</a>', item[0])[0][2])




