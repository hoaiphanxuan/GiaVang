from datetime import date
import json
import getData

def checkDataInFile():
    today=date.today()

    d1=today.strftime("%Y%m%d")
    print(d1)
    

#gD.listValue
checkDataInFile()