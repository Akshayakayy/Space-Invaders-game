import pygame

class missiles:
    def __init__(self, x, y, type):
      self.x = x
      self.y = y
      self.type = type

class m1(missiles):
    def bullet(self,screen):
        pygame.draw.circle(screen,(255,255,0),(int(self.x)+50,int(self.y)),8,8)


class m2(missiles):
    def bullet(self,screen):
        pygame.draw.rect(screen,(110,0,255),[int(self.x)+44,int(self.y),15,15])
