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
        
        with open('./data.json', mode='r') as file:
            data:dict = json.load(file)
        
        data.update(new_data)
        
        with open('./data.json', mode='w') as file:
            json.dump(data,file,indent=2)
        
    def delete_pass(self):
        pass
    
    def search_pass(self):
        pass
    
    def show_pass(self):
        pass