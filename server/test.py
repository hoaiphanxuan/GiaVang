from datetime import date
import json
import getData

def checkDataInFile():
    today=date.today()

    d1=today.strftime("%Y%m%d")
    print(d1)
    

#gD.listValue
with open('data.json',mode='r',encoding='utf-8') as file:
    data=json.load(file)
    print(data)

with open('./data/20211201.json',mode='w',encoding='utf-8') as file:
    file.write(str(data))