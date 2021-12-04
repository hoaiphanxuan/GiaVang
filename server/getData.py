import requests, json
import os
from bs4 import BeautifulSoup
from datetime import date
import threading
import time
from threading import Thread

def getDataFromWeb():
	response = requests.get("https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now")
	#soup = BeautifulSoup(response.content, "html.parser")

	data = response.content.decode('UTF-8-sig')
	#data kiểu là string
	#chuyển kiểu dữ liệu của data từ string sang dict (có cấu trúc tương tự json)
	js=json.loads(data)

	#sử dụng phương thức get() của dict lấy ra các giá trị của golds =>js1 lúc này có kiểu list
	js1=js.get('golds')

	#js1[0] => lấy phần đầu của danh sách; js1[0] có kiểu dict =>js1[0].get('value') có kiểu list 
	js2 = js1[0].get('value')
	return js2

def checkExistFile():
	today=date.today()
	d1=today.strftime("%Y%m%d")
	filepath='./data/'+d1+'.json'
	if(os.path.isfile(filepath)==False):
		dataWeb=getDataFromWeb()
		with open(filepath,mode='w',encoding='UTF-8') as file:
			json.dump(dataWeb,file)
			#file.write(str(dataWeb))
			
def updateDataEvery30Min(a):
	while (1):
		time.sleep(30*60)
		dataWeb=getDataFromWeb()
		today=date.today()
		d1=today.strftime("%Y%m%d")
		filepath='./data/'+d1+'.json'
		dataWeb=getDataFromWeb()
		with open(filepath,mode='w',encoding='UTF-8') as file:
			json.dump(dataWeb,file)
