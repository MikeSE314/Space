import pygame

class Keys:
    def __init__(self):
        self.keysPressed = pygame.key.get_pressed()
    def get_pressed_keys(self):
        self.keysPressed = pygame.key.get_pressed()
    def get_keys(self):
        return self.keysPressed