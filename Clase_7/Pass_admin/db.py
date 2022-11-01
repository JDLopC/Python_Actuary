import json



class Database:
    def __init__(self):
        pass
    
    def add_pass(self, *args):
        web = args[0]
        user = args[1]
        passwrod = args[2]
        
        new_data = {
            web: {
                'user':user,
                'password': passwrod
            }
        }
        
        data = self.load_json()
        
        data.update(new_data)
        
        self.update_json(data)
        
    def delete_pass(self, web):
        data = self.load_json()
        
        if web in data.keys():
            del data[web]
            self.update_json(data)
        else:
            print('La web no existe, intente de nuevo')
            input('Presione enter para continuar')
        
    
    def search_pass(self, web):
        data = self.load_json()
        
        if web in data.keys():
            print(data[web])
        else:
            print('La web no existe, intente de nuevo')
            input('Presione enter para continuar')
            
    
    def show_pass(self):
        pass
    
    def load_json(self):
        with open('./data.json', mode='r') as file:
            data:dict = json.load(file)
        return data
    
    def update_json(self, data):
        with open('./data.json', mode='w') as file:
            json.dump(data,file,indent=2)