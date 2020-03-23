import requests

#from pages import serializers
login=False
s=requests.Session()
while(True):
        input1=input('please input your command:')
        input1=input1.split()
        if len(input1)<1:
                print('you can choice the command from: list, view, average, rate, register, login, logout')                
        if input1[0]== 'list':
                response = requests.get("http://127.0.0.1:8000/module")
                #serializer = serializer.ModuleSerializer(response.text)
                #print(response.text)
                data=response.json()
                print('Code            Name                 Year   Semester   Taught by')
                for moduleInstance in data:
                        print('{:^6s}{:^30s}{:^7d}{:^3d}{:^6s}{:^5s}{:<20s}'.format(moduleInstance['module']['module_id'],moduleInstance['module']['name'],moduleInstance['year'],moduleInstance['semester'],' ',moduleInstance['professor'][0]['professor_id'],moduleInstance['professor'][0]['name']))
                        if len(moduleInstance['professor'])>1:
                                for professor in moduleInstance['professor'][1:]:
                                        print(' '*53+professor['professor_id']+' '+professor['name'])
                        print('-'*63)
                        #print(module)
        elif input1[0]== 'view':
        #headers={'professor_id':input[1]}
        #headers['module_id']=input[2]
        #response = requests.get("http://127.0.0.1:8000/view", params = headers)
                response = requests.get("http://127.0.0.1:8000/view")
                data=response.json()
                for professor in data:
                        print('The rating of Professor %s (%s) is %d.'%(professor['name'],professor['id'],professor['rating']))
                #print(response.text)
        elif input1[0]== 'average':
                if len(input1)==3:
                        headers={'professor_id':input1[1]}
                        headers['module_id']=input1[2]        
                        response = requests.get("http://127.0.0.1:8000/average", params = headers)
                        if response.text=='not found':
                                print("found no record with given professor id and module code,the professor may not teach this module")
                        elif response.text=='no rating':
                                print("the professor have not receive rating on this module yet")
                        else:
                                data=response.json()
                                print('The rating of Professor %s (%s) in module %s (%s) is %d.'%(data['professor_name'],input1[1],data['module_name'],input1[2],data['rating']))
                                
                else:
                        print('you need to declare in following form: average professor_id module_code')
        elif input1[0]== 'rate':
                if len(input1)==6:
                        print(type(input1[5]))
                        params={'professor_id':input1[1]}
                        params['module_id']=input1[2]
                        params['year']=input1[3]
                        params['semester']=input1[4]
                        params['rating']=input1[5]
                        if login==True:
                                response = s.get("http://127.0.0.1:8000/rate", params = params)
                                if response.text=='rate success':
                                        print('rate successfully')
                                else:
                                        print('rate failed,you may provide wrong info about the professor or the module instance.')
                        else:
                                print('you have to login before rating')
                else:
                        print('you need to declare in following form: rate professor_id module_id year semester rating')
        elif input1[0]== 'register':
                username=input('please input username:')
                params={'username':username}
                email=input('please input email:')
                params['email']=email
                password=input('please input password:')
                params['password']=password
                response = requests.get("http://127.0.0.1:8000/register", params = params)
                if response.text=='success register':
                        print('register successfully')
                else:
                        print('register failed,user with given username already existed')
        elif input1[0]== 'login':
                username=input('please input username:')
                params={'username':username}
                password=input('please input password:')
                params['password']=password
                response = s.get("http://127.0.0.1:8000/login", params = params)
                if response.text=='success login':
                        login=True
                        print('login successfully')
                else:
                        print('login failed,you may check your username or password')
        elif input1[0]== 'logout':
                response = s.get("http://127.0.0.1:8000/logout")
                if response.text=='logout':
                        print('logout successfully')
                        login=False
        else:
                print('you can choice the command from: list, view, average, rate, register, login, logout')