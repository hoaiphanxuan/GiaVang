import requests, json

from bs4 import BeautifulSoup

response = requests.get("https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now")

#soup = BeautifulSoup(response.content, "html.parser")

data = response.content.decode('UTF-8-sig')

#print(data)
print(type(data))

#chuyển kiểu dữ liệu của data từ string sang dict (có cấu trúc tương tự json)
js=json.loads(data)
print(type(js))
#sử dụng phương thức get() của dict lấy ra các giá trị của golds =>js1 lúc này có kiểu list
js1=js.get('golds')
print(type(js1))

#js1[0] => lấy phần đầu của danh sách; js1[0] có kiểu dict =>js1[0].get('value') có kiểu list 
js2 = js1[0].get('value')
print(js2)



input()