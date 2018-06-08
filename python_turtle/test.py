import turtle    # importing the module

ctx = turtle.Turtle()

screen = ctx.getscreen()
screen.register_shape("cat.gif")

# ctx.shape('cat.gif')

ctx.penup()
ctx.setpos(-125, 10)
ctx.pendown()

ctx.pencolor('orange')
ctx.pensize(15)
ctx.speed(1)

ctx.forward(250)
ctx.right(90)
ctx.forward(80)
ctx.right(90)
ctx.forward(250)
ctx.right(90)
ctx.forward(80)
ctx.penup()

ctx.setpos(-80,-50)
ctx.pendown()

ctx.pencolor('orange') 
ctx.write('LeapLearner', font=("Arial", 20, "bold"))

ctx.penup()

ctx.ht()
