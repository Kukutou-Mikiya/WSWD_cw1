import requests
import urllib.request

#from pages import serializers
input1=input('please input your command:')
input1=input1.split()
if input1[0]== 'list':
        response = requests.get("http://127.0.0.1:8000/module")
        #serializer = serializer.ModuleSerializer(response.text)
        print(response.text)
elif input1[0]== 'view':
        #headers={'professor_id':input[1]}
        #headers['module_id']=input[2]
        #response = requests.get("http://127.0.0.1:8000/view", params = headers)
        response = requests.get("http://127.0.0.1:8000/view")
        print(response.text)
elif input1[0]== 'average':
        headers={'professor_id':input1[1]}
        headers['module_id']=input1[2]        
        response = requests.get("http://127.0.0.1:8000/average", params = headers)
        print(response.text)
elif input1[0]== 'rate':
        params={'professor_id':input1[1]}
        params['module_id']=input1[2]
        params['year']=input1[3]
        params['semester']=input1[4]
        params['rating']=input1[5]
        response = requests.get("http://127.0.0.1:8000/rate", params = params)
elif input1[0]== 'register':
        username=input('please input username:')
        params={'username':username}
        email=input('please input email:')
        params['email']=email
        password=input('please input password:')
        params['password']=password
        response = requests.get("http://127.0.0.1:8000/register", params = params)