import os
from multiprocessing import Process
from os import path
import hmac
from hashlib import sha1

try:
	import json
	import samino	
    
	import requests
	from pyfiglet import figlet_format
except:
	os.system("pip install samino -U")
	os.system("pip install json-minify")
	os.system("pip install requests")
	os.system("pip install requests")
	os.system("pip install pyfiglet")
	import samino
	import requests
	from pyfiglet import figlet_format
	

identifier = os.urandom(20)
x= ("42" + identifier.hex() + hmac.new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()
devi = x
print(figlet_format("By Lord", font="doom", width=64))

#var
chatLink = input ("chatLink >>")
data = open("accounts.json")
accs = json.load(data)


client = samino.Client(devi)
path = client.get_from_link(chatLink)
comId = path.comId
chatId = path.objectId

def run():
	identifier = os.urandom(20)
	x= ("42" + identifier.hex() + hmac.new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()
	devi = x
	client = samino.Client(devi)
	try:
		client.login(email,password)
		print(f"logged in{email}")
		client.join_community(comId)
		samino.Local(comId).join_chat(chatId)
		client.socketClient.joinVideoChatAsSpectator(comId, chatId)
		print(f"join{email}")
	except Exception as e:
		print(e)
		pass
for acc in accs:
	email = acc["email"]
	password = acc["password"]
	deviceId = acc["device"]
	pps = []
	p1 = Process(target=run)
	p1.start()
	pps.append(p1)
for pp in pps:
	pp.join()