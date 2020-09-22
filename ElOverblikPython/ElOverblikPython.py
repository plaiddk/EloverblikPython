import requests
import json
import os

#Creating Bearer auth
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


 #Get token from api
token = requests.get('https://api.eloverblik.dk/CustomerApi/api/Token', auth=BearerAuth('insert token from eloverblik.dk'))

#Dump result to json
tokendump =  json.dumps(token.json())
jsonstring = json.loads(tokendump)
tokenacces =jsonstring["result"]

#Get Meter data
body = '{"meteringPoints": {"meteringPoint": ["INSERT meteringpoint"] }}'
meterdata = requests.post('https://api.eloverblik.dk/CustomerApi/api/MeterData/GetTimeSeries/2020-01-01/2020-02-01/Hour', auth=BearerAuth(tokenacces),data=body.encode('utf8'),headers = {'Content-type': 'application/json'})
print(meterdata.status_code)   

#Dump meterdata to json
meterdump=  json.dumps(meterdata.json())         

#Change directory to write json
os.getcwd()
os.chdir(r"D:\\testdata\\")

#Write json to file
newfile = open("meterdata.json","w")
newfile.write(meterdump)
