import pygame

class Ship():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/fighter.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
    	if self.moving_left and self.rect.right < self.screen_rect.right:
    		self.centerx -= self.ai_settings.ship_speed_factor
    	elif self.moving_right and self.rect.left > 0:
    		self.centerx += self.ai_settings.ship_speed_factor

    	self.rect.centerx = self.centerx	

    def blitme(self):
        """ draw image on screen """
        self.screen.blit(self.image, self.rect)
