import requests, json

from bs4 import BeautifulSoup

response = requests.get("https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now")

#soup = BeautifulSoup(response.content, "html.parser")

data = response.content.decode('UTF-8-sig')

#print(data) data kiểu là string


#chuyển kiểu dữ liệu của data từ string sang dict (có cấu trúc tương tự json)
js=json.loads(data)

#sử dụng phương thức get() của dict lấy ra các giá trị của golds =>js1 lúc này có kiểu list
js1=js.get('golds')

#js1[0] => lấy phần đầu của danh sách; js1[0] có kiểu dict =>js1[0].get('value') có kiểu list 
js2 = js1[0].get('value')
#print(js2)

listValue = []
for value in js2:
	listValue.append(value)
#getdata=json.dumps(listValue,indent=4)
#print(getdata)
with open('data.json',mode='w',encoding='UTF-8') as data:
	json.dump(listValue,data)

with open('data.json',mode='r',encoding='UTF-8') as data:
	getdata=json.load(data)
	print(getdata)
input()