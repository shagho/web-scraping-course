import requests

r = requests.get("https://www.varzesh3.com/ertty/456")
print("status_code:", r.status_code)
print("response text:", r.text)



