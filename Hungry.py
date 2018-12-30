# ::A Snake Game::
##Master
import pygame
import time
import random  # A COMMENT AREA:

#################################################################################################################################################

pygame.init()

width = 480
height = 480
gameDisplay = pygame.display.set_mode((width, height))  # Defines the display as well as size of it
pygame.display.set_caption("Hungry _ Snake!!")  # Gives caption to the game
White = (255, 255, 255)  # simple color defining
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
FPS = 10
clock = pygame.time.Clock()  # for definin the frame rate per secind clock is used
font = pygame.font.SysFont(None, 30)


##################################################################################################################################################

def snake(block_size, snakelist):
    for xny in snakelist:
        pygame.draw.rect(gameDisplay, green, [xny[0], xny[1], block_size, block_size])


##################################################################################################################################################
def text_objects(text, color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


###################################################################################################################################################

def message_to_screen(msg, color):
    """" screen_text = font.render(msg, True, color)
         gameDisplay.blit(screen_text, [0, height / 2])"""
    textsurf, textrect = text_objects(msg, color)
    textrect.center = (width / 2), (height / 2)
    gameDisplay.blit(textsurf, textrect)


##################################################################################################################################################

def gameloop():
    lead_x = 0
    lead_y = 0  # defining position of x and

    lead_x_change = 0  # for making the change in the game ## DIY
    lead_y_change = 0

    gameover = False
    gameexit = True

    block_size = 10
    snakelist = []
    snakelength = 1
    feedx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    feedy = round(random.randrange(0, height - block_size) / 10.0) * 10.0
    while gameexit:
        while gameover == True:
            gameDisplay.fill(White)
            message_to_screen("Game over ! Press C to continue and Q to quit", blue)
            pygame.display.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = False
                        gameexit = False
                    if event.key == pygame.K_c:
                        gameover = False
                        gameexit = True
                        gameloop()

        gameDisplay.fill(black)  # filll the backgroun color
        for event in pygame.event.get():  # loop fo rrepeating our event(Work being performed by our mouse or keyboard)
            if event.type == pygame.QUIT:  # exits the game if this condition comes via event
                gameexit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lead_x_change = +block_size
                    lead_y_change = 0
                elif event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = +block_size
                    lead_x_change = 0

        if lead_x >= height or lead_x < 0 or lead_y >= width or lead_y < 0:
            gameover = True

        lead_x = lead_x_change + lead_x
        lead_y = lead_y_change + lead_y

        pygame.draw.rect(gameDisplay, red, [feedx, feedy, block_size, block_size])
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                gameover = True
        snake(block_size, snakelist)

        pygame.display.update()  # This module updates everything over your screen
        clock.tick(FPS)  # This will help in determining your frame rates per second

        if feedx == lead_x and feedy == lead_y:
            feedx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            feedy = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snakelength += 1.5

    pygame.quit()
    quit()  # Quits the program


########################################################################################################################################################

gameloop()
