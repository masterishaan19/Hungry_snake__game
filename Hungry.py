# ::A Snake Game::
##Master
import pygame
import time
import random                                                                                     #A COMMENT AREA:
#################################################################################################################################################

pygame.init()

width = 1000
height =1000
gameDisplay = pygame.display.set_mode((width,height))                                   #Defines the display as well as size of it
pygame.display.set_caption("Hungry _ Snake!!")                                          #Gives caption to the game
img = pygame.image.load('head.png')
body = pygame.image.load('body.png')
#feed = pygame.image.load('cookie.png')
White = (255, 255, 255)                                                                   #simple color defining
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue=(0,0,255)
purple = (40, 32, 56)
yellow = (248, 184, 120)
orange = (216, 56, 124)
cyan = (96, 200, 216)
color = {
'White' : (255, 255, 255) ,
'green' : (0, 255, 0),
'red' : (255, 0, 0),
'blue' : (0,0,255),
'yellow' : (248, 184, 120),
'orange' : (216, 56, 124),
'cyan' : (96, 200, 216)
}
color_keys = list(color.keys())
print(color_keys)
colors = random.choice(color_keys)
FPS = 8
direction = "right"
bonus = 2
clock = pygame.time.Clock()  # for definin the frame rate per secind clock is used
##################################################################################################################################################

def snake(block_size,  snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    elif direction == "left":
        head = pygame.transform.rotate(img, 90)
    elif direction == "up":
        head = img
    elif direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for xny in snakelist[:-1]:
        #pygame.draw.rect(gameDisplay, color[colors], [xny[0], xny[1], block_size, block_size])
        gameDisplay.blit(body, (xny[0], xny[1]))
##################################################################################################################################################
smallfont = pygame.font.SysFont("comicsansms", 20)
mediumfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 60)
def text_objects(text, color, size):
    if size == "small":
        textsurface =smallfont.render(text,True,color)
    elif size == "medium":
        textsurface =mediumfont.render(text,True,color)
    elif size == "large":
        textsurface =largefont.render(text,True,color)
    return textsurface, textsurface.get_rect()
###################################################################################################################################################
def pause():
    paused =True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(yellow)
        message_to_screen("PAUSED", black, -200, size="large")
        message_to_screen(" Press 'Space' to resume or 'Q' to quit", orange, 100, size="medium")
        pygame.display.update()
#################################################################################################################################################

def message_to_screen(msg, color,y_displace=0, size="small", x_displace=0):
    """" screen_text = font.render(msg, True, color)
         gameDisplay.blit(screen_text, [0, height / 2])"""
    textsurf, textrect =text_objects(msg, color, size)
    textrect.center =(width/2)-x_displace, (height/2)+y_displace
    gameDisplay.blit(textsurf, textrect)

##################################################################################################################################################
def game_intro():
    intro = True
    while intro:
        gameDisplay.fill(blue)
        message_to_screen("Welcome to Hungry_Snake GAME:", green, -400, size="large")
        message_to_screen("Objective of the game is to eat red dots!!", black, -100, size="medium",x_displace=10)
        message_to_screen("As you eat -> You Grow", black, 0, size="medium", x_displace=184)
        message_to_screen("As you eat -> You Get Faster", black, -50, size="medium",x_displace=134)
        message_to_screen("Rules:", White, 150, size="medium", x_displace=440)
        message_to_screen("1. Use arrow keys to move !", White, 190, size="small", x_displace=364)
        message_to_screen("2. While moving horizontally only use up or down key", White, 210, size="small", x_displace=250)
        message_to_screen("3. While moving vertically only use left or right key", White, 230, size="small",x_displace=256)
        message_to_screen("4. using other keys then specified would lead to a loose", White, 250, size="small",x_displace=236)
        message_to_screen("5. Try no to run into yourself!", White, 270, size="small",x_displace=356)
        message_to_screen("6. Otherwise you will loose", White, 290, size="small",x_displace=368)
        message_to_screen(":::::::::::::::::::::::::::::::::Impotant Tips:::::::::::::::::::::::::::::::::", purple, 380, size="medium")
        message_to_screen(":Press C to Start and Q to quit game:", White, 430, size="small")
        message_to_screen(":Press Space to pause the game:", White, 470, size="small")
        message_to_screen(":Press R to Restart the game:", White, 450, size="small")

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameloop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

##################################################################################################################################################
def gameloop():
    FPS = 8
    global direction
    global colors
    global bonus
    direction = "right"
    score = 0
    limit=5

    lead_x = 0
    lead_y = 0                                                                              # defining position of x and

    lead_x_change = 20                                                                      # for making the change in the game ## DIY
    lead_y_change = 0

    gameover = False
    gameexit = True

    block_size = 20
    snakelist = []
    snakelength = 1
    feedx = round(random.randrange(0,width-block_size)/20.0)*20.0
    feedy = round(random.randrange(0,height-block_size)/20.0)*20.0
    bonus_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    bonus_y = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    colors = random.choice(color_keys)
    while gameexit:
        while gameover == True:
            gameDisplay.fill(purple)
            message_to_screen("Game over!! ", red , -300, size="large")
            message_to_screen("Press C to restart and Q to quit", White , 50, size="medium")
            message_to_screen("Your Score:", White, -100, size="medium")
            message_to_screen(string, White,-100, size="medium", x_displace=-150)
            pygame.display.update()
            for event in pygame.event.get():
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

        gameDisplay.fill(black)                                                             #filll the backgroun color
        for event in pygame.event.get():                                                    #loop fo rrepeating our event(Work being performed by our mouse or keyboard)
            if event.type == pygame.QUIT:                                                   #exits the game if this condition comes via event
                gameexit=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = +block_size
                    lead_y_change = 0
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = +block_size
                    lead_x_change = 0
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    gameloop()
                elif event.key == pygame.K_SPACE:
                    pause()


        if lead_x >= height or lead_x< 0 or lead_y >= width or lead_y < 0:
            gameover = True

        lead_x = lead_x_change + lead_x
        lead_y = lead_y_change + lead_y

        pygame.draw.rect(gameDisplay, color[colors],[feedx,feedy, block_size, block_size])
        if bonus % 3 ==0 :
            pygame.draw.rect(gameDisplay, color[colors], [bonus_x, bonus_y, block_size, block_size])
            bonus += 4
            score

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        print(snakelist)
        print(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            print(snakelist)
            if eachSegment == snakehead:
                gameover=True
        snake(block_size,  snakelist)
        clock.tick(FPS)

        if feedx== lead_x and feedy== lead_y:
            feedx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            feedy = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            colors = random.choice(color_keys)
            snakelength += 1.0
            score += 1

            if score >= limit:
                FPS += 5
                limit += 5

        if bonus_x == lead_x and bonus_y == lead_y:
            bonus_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            bonus_y = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            score += 5

        string = str(score)
        message_to_screen("Score:", White, y_displace=-490, size="small")
        message_to_screen(string, White, y_displace=-490, size="small", x_displace=-50)
        pygame.display.update()

    pygame.quit()
    quit()                                                                                   #Quits the program
########################################################################################################################################################
game_intro()

