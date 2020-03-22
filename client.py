import requests
import urllib.request

#from pages import serializers
input=input('please input your command:')
input=input.split()
if input[0]== 'list':
        response = requests.get("http://127.0.0.1:8000/module")
        #serializer = serializer.ModuleSerializer(response.text)
        print(response.text)
elif input[0]== 'view':
        #headers={'professor_id':input[1]}
        #headers['module_id']=input[2]
        #response = requests.get("http://127.0.0.1:8000/view", params = headers)
        response = requests.get("http://127.0.0.1:8000/view")
        print(response.text)
elif input[0]== 'average':
        headers={'professor_id':input[1]}
        headers['module_id']=input[2]        
        response = requests.get("http://127.0.0.1:8000/average", params = headers)
        print(response.text)
elif input[0]== 'rate':
        params={'professor_id':input[1]}
        params['module_id']=input[2]
        params['year']=input[3]
        params['semester']=input[4]
        params['rating']=input[5]
        response = requests.get("http://127.0.0.1:8000/rate", params = params)