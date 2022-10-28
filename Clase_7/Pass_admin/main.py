from db import Database
from UI import UI


db = Database()
interfaz = UI(db)



interfaz.main_loop()