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
    _x = 0.0
    _y = 0.0

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

    """
    New methods to change the private variables for the sprite position.
    I think the game sprite will officially be called 'Block' if this goes on!
    (^_^)
    """

    def setX(self, given):

        self._x = self._x + given

    def setY(self, given):

        self._y = self._y + given

    def setBoth(self, givenX, givenY):

        self._x = self._x + givenX
        self._y = self._y + givenY

    def getBoth(self):

        return (self._x, self._y)
