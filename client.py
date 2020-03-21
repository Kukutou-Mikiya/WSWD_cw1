import requests
#from pages import serializers
input=input('please input your command:')
input=input.split()
if input[0]== 'list':
        response = requests.get("http://127.0.0.1:8000/module")
        #serializer = serializer.ModuleSerializer(response.text)
        print(response.text)
#elif input[0]== 'list':