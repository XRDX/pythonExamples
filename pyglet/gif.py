import pyglet

animation = pyglet.image.load_animation('animation.gif')
bin = pyglet.image.atlas.TextureBin()
animation.add_to_texture_bin(bin)
sprite = pyglet.sprite.Sprite(img=animation)

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()