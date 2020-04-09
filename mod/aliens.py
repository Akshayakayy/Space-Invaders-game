import random

class aliens:
    def __init__(self, x, y, img, alien_count):
      self.x = x
      self.y = y
      self.img = img
      self.alien_count = alien_count

    def spawn(self,screen):
        screen.blit(self.img,(self.x,self.y))
        return
