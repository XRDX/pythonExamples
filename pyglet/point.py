import pyglet

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    vertex_list = pyglet.graphics.vertex_list(2,
        ('v2i', (10, 15, 30, 35)),
        ('c3B', (0, 0, 255, 0, 255, 0))
    )
    vertex_list.draw(pyglet.gl.GL_POINTS)

pyglet.app.run()