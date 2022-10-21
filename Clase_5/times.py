# Clase, que contenga métodos para cambiar de formado de horas
# Si nos dan horas en el formato de 24:00 las quiero en minutos
# Si nos dan minutos, las quiero en formato de 24:00



# Input: str, '16:55'

MORNING = '07:15'
AFTERNOON = '19:00'
class Converter:
    def hours_to_minutes(self, time:str):
        datos = time.split(':')

        datos[0] = int(datos[0])
        datos[1] = int(datos[1])
        
        minutes = datos[0]*60 + datos[1]
        
        return minutes

    def minutes_to_hours(self, minutes:int):
        horas = int(minutes/60)
        mins = int(minutes % 60)
        
        respuesta = f"{horas}:{mins}"
        
        return respuesta

# solution = Converter()
# print(solution.hours_to_minutes('16:55'))
# print(solution.minutes_to_hours(solution.hours_to_minutes('17:35')))