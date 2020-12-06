"""
Author: Ryan Baclit
Email: gamehelphere@gmail.com
License: GPL 2.0
"""
import pygame

class BGDemo:

    screenWidth = 1024
    screenHeight = 768
    screen = ""
    gameIsRunning = True

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("BGDemo - Basic Game Demo")
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

    def draw(self):

        pass

    def main(self):
        event = ""
        pressedKeys = []

        while self.gameIsRunning:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    pressedKeys = pygame.key.get_pressed()
                    print(pressedKeys[pygame.K_q])
                    if pressedKeys[pygame.K_q] == True:
                        gameIsRunning = False

            self.draw()

if __name__=="__main__":

    bgdemo = BGDemo()
    bgdemo.main()
