"""
Author: Ryan Baclit
Email: gamehelphere@gmail.com
License: GPL 2.0
"""
import pygame
import os
from Block import Block

class BGDemo:

    screenWidth = 640
    screenHeight = 480
    screen = ""
    gameIsRunning = True
    _block = ""

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("BGDemo - Basic Game Demo")
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        print(os.getcwd())
        self.block = Block(os.getcwd() + "/images/player.png")

    def draw(self):

        self.screen.blit(self.block.image, (0, 0))

        pygame.display.flip()

    def main(self):
        event = ""
        pressedKeys = []

        while self.gameIsRunning:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    pressedKeys = pygame.key.get_pressed()
                    print("event.key")
                    print(event.key)
                    print("pygame.K_q")
                    print(pygame.K_q)

                    # If the key that was pressed and released is the same as the 'q' key, exit game.

                    if event.key == pygame.K_q:
                        self.gameIsRunning = False
                    else:
                        print("wala.")

            self.draw()

if __name__=="__main__":

    bgdemo = BGDemo()
    bgdemo.main()
