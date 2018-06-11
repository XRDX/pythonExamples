import pygame

COLORS = {
    "red" : (255, 0, 0),
    "white" : (255, 255, 255),
    "black" : (0, 0, 0),
    "green" : (0, 255, 0),
    "grey" : (100, 100, 100),
    "orange" : (255, 125, 0)
}

class Game():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    def init(self):
        pygame.init()
        pygame.display.set_caption("LeapLearner")

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                self.running = False
                pygame.quit()

    def run(self, func):
        self.init()

        while self.running:
            self.handle_event()

            func()

            #Refresh Screen
            pygame.display.flip()
            #Number of frames per secong e.g. 60
            self.clock.tick(50)

class Canvas():
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 400))
        self.w = self.screen.get_rect().width
        self.h = self.screen.get_rect().height

    def clear(self):
        self.screen.fill(COLORS["white"])
        #Draw The Road

class Rectangle():
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fillStyle = "orange"

    def draw(self):
        pygame.draw.rect(canvas.screen, getColor(self.fillStyle), (self.x, self.y, self.w, self.h))

def getColor(color):
    if(color.lower() in COLORS):
        return COLORS[color.lower()]
    else:
        return (255, 125, 0)

canvas = Canvas()
game = Game()
run = game.run

def rectangle(x, y, w, h, c):
    pygame.draw.rect(canvas.screen, getColor(c), (x, y, w, h))

