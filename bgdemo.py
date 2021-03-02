"""
Author: Ryan Baclit
Email: gamehelphere@gmail.com
License: GPL 2.0
"""
import pygame
import os
from Block import Block

class BGDemo:

    _screenWidth = 640
    _screenHeight = 480
    _screen = ""
    _gameIsRunning = True
    _block = ""
    _background = ""
    _blockBaddie = ""
    _spriteGroup = ""

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("BGDemo - Basic Game Demo")
        self._screen = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        print(os.getcwd())
        self._block = Block(os.getcwd() + "/images/player.png")
        self._block.setName("Hero")
        self._blockBaddie = Block(os.getcwd() + "/images/baddie.png")
        self._blockBaddie.setName("Villain")

        """
        Make a basic background image using a Surface filled with the color black. This will
        be changed later to some other game-related image.
        """

        self._background = pygame.Surface((self._screenWidth, self._screenHeight))
        self._background.fill(pygame.Color(0, 0, 0, 1))

        """
        Add sprites into a pygame.sprite.Group.
        """

        self._spriteGroup = pygame.sprite.Group()
        self._spriteGroup.add(self._block, self._blockBaddie)

        """
        Set initial coordinates of sprites.
        """

        self._blockBaddie.setBoth(150, 20)

    def draw(self):

        # First call the update() of the pygame.sprite.Group instance.

        self._spriteGroup.update()

        # Second draw the background.

        self._screen.blit(self._background, (0, 0))

        # Third draw the sprite.

        self._screen.blit(self._block.image, self._block.getBoth())
        self._screen.blit(self._blockBaddie.image, self._blockBaddie.getBoth())

        # Fourth do a display update.

        pygame.display.flip()

    def main(self):
        event = ""
        pressedKeys = []

        while self._gameIsRunning:

            """
            Grab an event from the queue. The following code will control the game loop's termination.
            This code is the first part solely for game loop control.
            """

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    # If the key that was pressed and released is the same as the 'q' key, exit game.

                    if event.key == pygame.K_q:
                        self._gameIsRunning = False

            """
            Handle game input by accessing queue continuously. This is needed to allow the
            full immersion and control for the player.
            
            This is the second part of event handling solely for player controls.
            """

            pressedKeys = pygame.key.get_pressed()

            """
            The rest of the keys will follow the a, s, d, and w keys used for most games.
            """

            if pressedKeys[pygame.K_a]:
                self._block.setX(-10.5)
            elif pressedKeys[pygame.K_s]:
                    self._block.setY(10.5)
            elif pressedKeys[pygame.K_d]:
                    self._block.setX(10.5)
            elif pressedKeys[pygame.K_w]:
                    self._block.setY(-10.5)

            self.draw()

            # Let pygame handle the internal event queue manipulation.

            pygame.event.pump()


if __name__=="__main__":

    bgdemo = BGDemo()
    bgdemo.main()
