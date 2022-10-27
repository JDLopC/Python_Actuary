class Perro:
    def __init__(self, nombre, sonido):
        self.name = nombre
        self.sound = sonido

    def saludo(self):
        print(f'soy un perro, me llamo {self.name}, mi sonido es {self.sound}')

perro1 = Perro('firulais', 'wow')
perro1.saludo()
perro2 = Perro('Bayo', 'wow')