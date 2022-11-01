import os
from db import Database
# Variable que haga tracking de en que menu estamos
# Una variable que nos diga si el programa tiene que seguir corriendo

class UI:
    
    def __init__(self, mydb:Database):
        self.db = mydb
        self.menu = 0
        self.running = True
    
    def main_menu(self):
        print('--Bienvenido a su gestor--')
        print('1.Agregar contra')
        print('2.Eliminar contra')
        print('3.Buscar contra')
        print('4.Mostrar contra')
        print('5.Salir del programa')
        self.menu = int(input('Escribe tu opcion: '))
        
       
    def add_pass(self):
        web = input('Ingrese web/aplicacion: ')
        user = input('Ingrese usuario: ')
        password = input('Ingrese contra: ')
        self.db.add_pass(web, user, password)
        self.menu = 0
    
    def delete_pass(self):
        web = input('Ingrese web/aplicacion a eliminar: ')
        self.db.delete_pass(web)
        self.menu = 0
    
    def search_pass(self):
        web = input('Ingrese web/aplicacion a buscar: ')
        self.db.search_pass(web)
        self.menu = 0
    
    def show_pass(self):
        print('Imprimir todas las contras')
        self.db.show_pass()
        self.menu = 0
    
    def exit(self):
        self.running = False
        print('Chao')
    
    def main_loop(self):
        while self.running:
            os.system('clear')
            if self.menu == 0:
                self.main_menu()
            elif self.menu == 1:
                self.add_pass()
            elif self.menu == 2:
                self.delete_pass()
            elif self.menu == 3:
                self.search_pass()
            elif self.menu == 4:
                self.show_pass()
            elif self.menu == 5:
                self.exit()
            else:
                print('No seleccionaste un opcion correcta')
                self.menu = 0