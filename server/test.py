import json
import io

username="hoaiphanxuan"
passwork="leomessi"
print(f"{username}")
lisUser=[]
with open('account.json',mode='r+',encoding="utf-8") as acc:
        data=json.load(acc)
        for user in data:
            if(user['username']==username):
               print('no')
            else:
            	lisUser.append(user)
        dic={"username":f"{username}","pass":f"{passwork}"}
        lisUser.insert(0,dic)
        print(lisUser)
with open('account.json',mode='w',encoding="utf-8") as acc:
	json.dump(lisUser,acc)