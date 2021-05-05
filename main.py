
import pygame
import random
import time


x = pygame.init()

#colors
white = (255,255,255)
green = (0,0,0)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)


game_width = 1200
game_height = 600
#creating window
gameWindow = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('Game Window')
pygame.display.update()

#clock..
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)
def text_screen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def rolling(points):

    if points == 1:
        pygame.draw.circle(gameWindow,white,(600,250),10)

    elif points == 2:
        pygame.draw.circle(gameWindow, white, (580, 250), 10)
        pygame.draw.circle(gameWindow, white, (620, 250), 10)

    elif points == 3:
        pygame.draw.circle(gameWindow, white, (570, 230), 10)
        pygame.draw.circle(gameWindow, white, (600, 250), 10)
        pygame.draw.circle(gameWindow, white, (630, 270), 10)

    elif points == 4:
        pygame.draw.circle(gameWindow, white, (580, 230), 10)
        pygame.draw.circle(gameWindow, white, (580, 270), 10)
        pygame.draw.circle(gameWindow, white, (620, 230), 10)
        pygame.draw.circle(gameWindow, white, (620, 270), 10)

    elif points == 5:
        pygame.draw.circle(gameWindow, white, (580, 230), 10)
        pygame.draw.circle(gameWindow, white, (580, 270), 10)
        pygame.draw.circle(gameWindow, white, (620, 230), 10)
        pygame.draw.circle(gameWindow, white, (620, 270), 10)
        pygame.draw.circle(gameWindow, white, (600, 250), 10)

    elif points == 6:

        pygame.draw.circle(gameWindow, white, (570, 230), 10)
        pygame.draw.circle(gameWindow, white, (600, 230), 10)
        pygame.draw.circle(gameWindow, white, (630, 230), 10)
        pygame.draw.circle(gameWindow, white, (570, 270), 10)
        pygame.draw.circle(gameWindow, white, (600, 270), 10)
        pygame.draw.circle(gameWindow, white, (630, 270), 10)

def welcome():
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        gameWindow.fill(green)
        text_screen("WELCOME!", blue, 500, 200)
        text_screen(" Press SPACEBAR to continue...", blue, 350, 300)

        pygame.display.update()
        clock.tick(30)

def gameloop():

    points = 6
    exit_game = False
    fps = 30

    while not exit_game:

        roll_dice = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll_dice = True

        gameWindow.fill(green)
        text_screen(" Press SPACEBAR to roll the dice...", blue, 300, 350)
        pygame.draw.rect(gameWindow, red, [550, 200, 100, 100])
        if roll_dice:
            roll = random.randint(15, 20)
            for j in range(roll):
                points = random.randint(1, 6)
                pygame.draw.rect(gameWindow, red, [550, 200, 100, 100])
                rolling(points)
                pygame.display.update()
                time.sleep(0.1)

        else:
            rolling(points)
            # print(points)
            pygame.display.update()
            clock.tick(fps)


welcome()
