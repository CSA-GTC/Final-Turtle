#Gregory Clarke
#Computor Programming
#9/15/2017

def draw_circle1():
    import turtle

    wn=turtle.Screen()
    wn.bgcolor("black")

    bob=turtle.Turtle()
    bob.color("green")
    bob.pensize(10)
    bob.speed(10)
    bob.fillcolor("purple")
    bob.begin_fill()

    for color in ("orange","blue","red","green","pink"):
        bob.stamp()
        bob.pencolor("black")
        bob.color(color)    
        bob.forward(250)
        bob.left(72)
    

    bob.end_fill()
   
    alex=turtle.Turtle()
    alex.color("green")
    alex.pensize(5)
    alex.speed(10)
    alex.fillcolor("purple")
    alex.begin_fill()

    for color in ("orange","blue","red","green","pink"):
        alex.stamp()
        alex.pencolor("black")
        alex.color(color)
        alex.forward(125)
        alex.left(72)
    

    alex.end_fill()
    
    wn.exitonclick()

draw_circle1()
