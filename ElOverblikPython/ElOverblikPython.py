import requests
import json
import os

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


token = requests.get('https://api.eloverblik.dk/CustomerApi/api/Token', auth=BearerAuth('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblR5cGUiOiJDdXN0b21lckFQSV9SZWZyZXNoIiwidG9rZW5pZCI6IjQ3NDIzNWJkLWZkMjYtNDYwNi1iNTFjLTc4MDU4YjNkNjE4OCIsImp0aSI6IjQ3NDIzNWJkLWZkMjYtNDYwNi1iNTFjLTc4MDU4YjNkNjE4OCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiUElEOjkyMDgtMjAwMi0yLTY1MTU5Mzg3NjUyOCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2dpdmVubmFtZSI6IlRob21hcyBSeXR0ZXIgSmVuc2VuIiwibG9naW5UeXBlIjoiS2V5Q2FyZCIsInBpZCI6IjkyMDgtMjAwMi0yLTY1MTU5Mzg3NjUyOCIsInR5cCI6IlBPQ0VTIiwiZXhwIjoxNjMxMTExMTc0LCJpc3MiOiJFbmVyZ2luZXQiLCJ0b2tlbk5hbWUiOiJ0aG9tYXMiLCJhdWQiOiJFbmVyZ2luZXQifQ.WMWuFoHRvXrAhmOJfNVmpNHTrmNbtRXxbvgS_B3grNA'))

jtopy =  json.dumps(token.json())
dict_json = json.loads(jtopy)

tokenacces =dict_json["result"]
body = '{"meteringPoints": {"meteringPoint": ["571313115400203473"] }}'
headers = {'Content-type': 'application/json'}

headers={'Content-type':'application/json', 'Accept':'application/json'}
meterdata = requests.post('https://api.eloverblik.dk/CustomerApi/api/MeterData/GetTimeSeries/2020-01-01/2020-02-01/Hour', auth=BearerAuth(tokenacces),data=body.encode('utf8'),headers = {'Content-type': 'application/json'})

jmeter=  json.dumps(meterdata.json())         
print(meterdata.status_code)   

os.getcwd()
os.chdir(r"D:\\testdata\\")

newfile = open("meterdata.json","w")
newfile.write(jmeter)
