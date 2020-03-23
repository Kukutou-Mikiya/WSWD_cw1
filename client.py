import requests

#from pages import serializers
login=False
s=requests.Session()
while(True):
        input1=input('please input your command:')
        input1=input1.split()                
        if input1[0]== 'list':
                response = requests.get("http://127.0.0.1:8000/module")
                #serializer = serializer.ModuleSerializer(response.text)
                #print(response.text)
                data=response.json()
                print('Code   Name                       Year   Semester    Taught by')
                for module in data:
                        print('{:^6s}{:^30s}{:^6d}{:^3d}{:>6s}{:<20s}'.format(module['module_id'],module['name'],module['year'],module['semester'],module['professor'][0]['professor_id'],module['professor'][0]['name']))
                        if len(module['professor'])>1:
                                for professor in module['professor'][1:]:
                                        print(' '*40+professor['professor_id']+' '+professor['name'])
                        #print(module)
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
                print(type(input1[5]))
                params={'professor_id':input1[1]}
                params['module_id']=input1[2]
                params['year']=input1[3]
                params['semester']=input1[4]
                params['rating']=input1[5]
                if login==True:
                        response = s.get("http://127.0.0.1:8000/rate", params = params)
                else:
                        print('you have to login before rating')
        elif input1[0]== 'register':
                username=input('please input username:')
                params={'username':username}
                email=input('please input email:')
                params['email']=email
                password=input('please input password:')
                params['password']=password
                response = requests.get("http://127.0.0.1:8000/register", params = params)
        elif input1[0]== 'login':
                username=input('please input username:')
                params={'username':username}
                password=input('please input password:')
                params['password']=password
                response = s.get("http://127.0.0.1:8000/login", params = params)
                if response.text=='success login':
                        login=True
                        print('success login')
                else:
                        print('failed login')
        elif input1[0]== 'logout':
                response = s.get("http://127.0.0.1:8000/logout")
                login=False