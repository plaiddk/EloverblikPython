import requests
import json
import os

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


token = requests.get('https://api.eloverblik.dk/CustomerApi/api/Token', auth=BearerAuth('insert token from eloverblik.dk'))

jtopy =  json.dumps(token.json())
dict_json = json.loads(jtopy)

tokenacces =dict_json["result"]
body = '{"meteringPoints": {"meteringPoint": ["INSERT meteringpoint"] }}'
headers = {'Content-type': 'application/json'}

headers={'Content-type':'application/json', 'Accept':'application/json'}
meterdata = requests.post('https://api.eloverblik.dk/CustomerApi/api/MeterData/GetTimeSeries/2020-01-01/2020-02-01/Hour', auth=BearerAuth(tokenacces),data=body.encode('utf8'),headers = {'Content-type': 'application/json'})

jmeter=  json.dumps(meterdata.json())         
print(meterdata.status_code)   

os.getcwd()
os.chdir(r"D:\\testdata\\")

newfile = open("meterdata.json","w")
newfile.write(jmeter)
