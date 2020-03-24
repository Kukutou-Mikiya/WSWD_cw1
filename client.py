import requests

#global parameters
login=False
s=requests.Session()
default_url='http://127.0.0.1:8000'
url='http://127.0.0.1:8000'

def moduleInstance_list():
        response = requests.get("%s/module"%(url))
        data=response.json()
        print('Code            Name                 Year   Semester   Taught by')
        for moduleInstance in data:
                print('{:^6s}{:^30s}{:^7d}{:^3d}{:^6s}{:^5s}{:<20s}'.format(moduleInstance['module']['module_id'],moduleInstance['module']['name'],\
                        moduleInstance['year'],moduleInstance['semester'],' ',moduleInstance['professor'][0]['professor_id'],moduleInstance['professor'][0]['name']))
                if len(moduleInstance['professor'])>1:
                        for professor in moduleInstance['professor'][1:]:
                                print(' '*53+professor['professor_id']+' '+professor['name'])
                print('-'*63)

def professorRating_view():
        response = requests.get("%s/view"%(url))
        data=response.json()
        for professor in data:
                print('The rating of Professor %s (%s) is %d.'%(professor['name'],professor['id'],professor['rating']))
                #print(professor['rating'])

def average(input1):
        if len(input1)==3:
                headers={'professor_id':input1[1]}
                headers['module_id']=input1[2]        
                response = requests.get("%s/average"%(url), params = headers)
                if response.text=='not found':
                        print("found no record with given professor id and module code,the professor may not teach this module")
                elif response.text=='no rating':
                        print("the professor have not receive rating on this module yet")
                else:
                        data=response.json()
                        print('The rating of Professor %s (%s) in module %s (%s) is %d.'%(data['professor_name'],input1[1],data['module_name'],input1[2],data['rating']))
                        #print(data['rating'])                       
        else:
                print('you need to declare in following form: average professor_id module_code')


def rate(input1):
        if len(input1)==6:
                if int(input1[5])<1 or int(input1[5])>5:
                        print('The rating scale is from 1 to 5')
                        return
                print(type(input1[5]))
                params={'professor_id':input1[1]}
                params['module_id']=input1[2]
                params['year']=input1[3]
                params['semester']=input1[4]
                params['rating']=int(input1[5])
                if login==True:
                        response = s.get("%s/rate"%(url), params = params)
                        if response.text=='rate success':
                                print('rate successfully')
                        else:
                                print('rate failed,you may provide wrong info about the professor or the module instance.')
                else:
                        print('you have to login before rating')
        else:
                print('you need to declare in following form: rate professor_id module_id year semester rating')

def register():
        username=input('please input username:')
        params={'username':username}
        email=input('please input email:')
        params['email']=email
        password=input('please input password:')
        params['password']=password
        response = requests.get("%s/register"%(url), params = params)
        if response.text=='success register':
                print('register successfully')
        else:
                print('register failed,user with given username already existed')

def login(input1):
        if len(input1)!=2:
                print('you need to declare in following form:login url')
                return False
        url_forlogin=input1[1]                
        username=input('please input username:')
        params={'username':username}
        password=input('please input password:')
        params['password']=password
        try:
                response = s.get("%s/login"%(url_forlogin), params = params)
                if response.text=='success login':                
                        print('login successfully')
                        return True
                else:
                        print('login failed,you may check your username or password')
                        return False    
        except:
                print('connect failed check your url')
                return False
    
while(True):
        input1=input('please input your command:')
        input1=input1.split()
        if len(input1)<1:
                print('you can choice the command from: list, view, average, rate, register, login, logout')                
        elif input1[0]== 'list':
                moduleInstance_list()
        elif input1[0]== 'view':
                professorRating_view()
        elif input1[0]== 'average':
                average(input1)
        elif input1[0]== 'rate':
                rate(input1)
        elif input1[0]== 'register':
                register()
        elif input1[0]== 'login':
                if login(input1)==True:
                        login=True
                        #url=input1[1]
        elif input1[0]== 'logout':
                response = s.get("%s/logout"%(url))
                if response.text=='logout':
                        print('logout successfully')
                        login=False
        else:
                print('you can choice the command from: list, view, average, rate, register, login, logout')


