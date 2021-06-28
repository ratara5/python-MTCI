import turtle
import math

#Variar color al dibujar la función e^x*cos^x
dic={x: 1.5*math.exp(-0.02*x)*math.sin(0.2*x) for x in range(-200,200) }
d=turtle
d.setup(1200,700,0,0)
d.showturtle()
d.shape("turtle")
d.pensize(2)
d.colormode(255)
d.penup()
d.goto(list(dic.keys())[0],dic[0])
d.pendown()
for items in dic.items():
    d.goto(items[0],items[1])
    d.pencolor(abs(int(items[0]-items[1])),abs(int(items[1])),abs(int(items[0])))
d.fillcolor(0,255,255)
d.mainloop()