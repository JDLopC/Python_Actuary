import turtle as t

# tim = t.Turtle()
# tim.shape('turtle')
# tim.color('brown')
# tim.left(90)
# tim.penup()
# tim.forward(50)
# tim.pendown()
# tim.forward(50)

start = -400

colores = ['pink', 'purple', 'blue', 'red', 'black', 'gray', 'green']
tortugas = []
for color in colores:
    tim = t.Turtle()
    tim.shape('turtle')
    tim.left(90)
    tim.color(color)
    tim.goto(start, 0)
    start = start + 100
    tortugas.append(tim)



for i, tim in enumerate(tortugas):
    tim.forward(50)
    
    if (i+1) % 2 != 0:
        tim.forward(50)

pantalla = t.Screen()
pantalla.exitonclick()