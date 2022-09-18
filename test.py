import requests

def sendRequest():
	return requests.get("https://www.google.com")	

print(sendRequest())
