import turtle

def draw_up():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
        
def draw_right():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
        
def draw_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
        
def draw_down():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

turtle.listen()
turtle.shape('turtle')
turtle.onkey(draw_up, 'd')
turtle.onkey(draw_right, 'w')
turtle.onkey(draw_left, 'a')
turtle.onkey(draw_down, 's')

turtle.mainloop()
