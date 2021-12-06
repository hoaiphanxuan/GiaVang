from datetime import date
import json
import threading
import time
from threading import Thread

def updateData(a):
    while (a):
        time.sleep(4)
        print('do something')
        


try:
    print('a')
    t=time.perf_counter()
    threadUpdate=threading.Thread(target=updateData,args=(1,))
    threadUpdate.start()
    for i in range(1,5):
        print(time.perf_counter()-t)
    print('load')
    threadUpdate.end()
except:
    print('error')