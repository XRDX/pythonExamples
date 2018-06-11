from lleg import *

rect = Rectangle(10, 10, 100, 50)
rect.fillStyle = "Red"

rect2 = Rectangle(40, 20, 50, 30)

def main():
    canvas.clear()

    rect.x += 1
    rect2.y += 1

    if(rect.x > canvas.w):
        rect.x = 0

    if(rect2.y > canvas.h):
        rect2.y = 0

    rect.draw()
    rect2.draw()

    rectangle(100, 100, 200, 50, 'red')

run(main)
