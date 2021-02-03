"""

Author: Ryan Baclit
Email: gamehelphere@gmail.com
License: GPL 2.0

This is based from the pygame docs. The link is

https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite

"""

import pygame

class Block(pygame.sprite.Sprite):

    _spriteName = "wala pa."

    # Constructor.

    def __init__(self, filename):

       # Call the parent class (Sprite) constructor

       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load(filename)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y

       # This will be useful for collision detection!

       self.rect = self.image.get_rect()
       #print(self.rect)

    def setName(self, newName):

        self._spriteName = newName

    def update(self):

        message = self._spriteName + " called update."
        print(message)
