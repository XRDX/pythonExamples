from pyglet import *
import math
import random

window = window.Window()
window.set_caption("LeapLearner")

image_bg = resource.image('bg.jpg')
image_enemy = resource.image('enemy.png')
image_enemy.anchor_x = 40
image_hero = resource.image('hero.png')
image_hero.anchor_x = 40

ORANGE = (255, 125, 0, 255)

asix = text.Label("x, y", color=ORANGE, y=5)
score_text = text.Label("score: 0", y=450)
logo = text.Label("LeapLearner", color=ORANGE, font_size=36,                           x=window.width//2, y=window.height//2,
                  anchor_x='center', anchor_y='center')

bg = sprite.Sprite(image_bg)
enemy = sprite.Sprite(image_enemy, x= 200, y=400)
hero = sprite.Sprite(image_hero, x=100, y=50)

score = 0


@window.event
def on_draw():
    window.clear()
    bg.draw()
    logo.draw()
    score_text.draw()
    enemy.draw()
    hero.draw()
    asix.draw()
    
@window.event
def on_mouse_motion(x, y, dx, dy):
    asix.text = "x: {:d}, y: {:d}".format(x, y)
    hero.x = x

def update(dt):
    global score
    enemy.y -= 200 * dt
    if(enemy.y < 0):
        enemy.y = window.height
        enemy.x = random.randint(0, window.width)

    if(collide(enemy, hero)):
        enemy.y = window.height
        enemy.x = random.randint(0, window.width)
        score += 1
        score_text.text = "score: " + str(score)

def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)

def collide(s1, s2):
    collision_distance = (s1.image.height/2 + s2.image.height/2)
    actual_distance = distance(s1.position, s2.position)

    return (actual_distance <= collision_distance)

clock.schedule_interval(update, 1/60)
app.run()
