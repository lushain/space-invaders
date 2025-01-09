import pygame                                             # Type 'pip install pygame in the cammand promt'
import random                                             # Type 'pip install random in the cammand promt'
import math


pygame.init()
screen = pygame.display.set_mode((800, 600))              # CREATING SCREEN
background = pygame.image.load('background.jpg')

pygame.display.set_caption("Space invaders")              # Title of the game

icon = pygame.image.load('spaceship.png')                 # A varialble for the icon of the game
pygame.display.set_icon(icon)                            # to display the icon

player_icon = pygame.image.load('space-invaders.png')     # A variable for player's icon
playerX = 365                                             # X coordinate
playerY = 500                                              # Y coordinate

playerX_change = 0

def player(x, y):
    screen.blit(player_icon,(x, y))                     # Function to display player_icon {there is supposed to be a comma after image name}

enemy_icon = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =[]
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_icon.append(pygame.image.load('alien.png'))            # A variable for enemy's's icon
    enemyX.append(random.randint(0,736))                          # X coordinate        enemyY.append(random.randint(50 ,150))                      # Y coordinate
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemy_icon[i], (x, y))              # Function to display enemy_icon {there is supposed to be a comma after image name}


bullet_icon = pygame.image.load('bullet.png')            # A variable for enemy's's icon
bulletX = 0                                       # X coordinate
bulletY = 480                                     # Y coordinate
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

red = (200, 0, 0)
brigth_red = (255,0 ,0)
green = (0, 200, 0)
brigth_green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0, 0 ,0)

def show_score(x,y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

over_text = pygame.font.Font('freesansbold.ttf',128)

def game_over_text():
    over_text = font.render('GAME OVER !!' , True, (255, 255, 255))
    screen.blit(over_text, (300, 150))

def on_button(x,y,text =''):
    font = pygame.font.Font('freesansbold.ttf', 5)
    button_text = font.render(text, True, (black))
    screen.blit(button_text, ((x + 5), (y + 5)))


def bullet(x, y):
    screen.blit(bullet_icon, (x, y))             # Function to display enemy_icon {there is supposed to be a comma after image name}

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon, (x+19, y+10))

def iscoalision(bulletX,bulletY,enemyX,enemyY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 25:
        return True
    else:
        return

running = True

while running :

    screen.fill((0, 0, 0))                         # to fill the screen with some color RGB = (red,green,blue)
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:          # If arrow key is pressed change value of playerX_change
            if event.key == pygame.K_LEFT:
                playerX_change = -0.75
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.75
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:                   # If arrow key is released stop changing value of playerX_change
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change                    #player movement
    if playerX <= 0:                             #(The boundary)
        playerX = 0
    elif playerX >= 736:                         #(     "      )
        playerX = 736

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                game_over_text()
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                pygame.draw.rect(screen, green, (100, 300, 200, 50))
                on_button(100,300,'play again?')

                if 100 + 200 > mouse[0] > 100 and 300 + 50 > mouse[1] > 300:   #for the x axis if cursor is more than the width and the x axis combined then it is inside same for y axis
                    pygame.draw.rect(screen, brigth_green, (100, 300, 200, 50))    # inside the bracket(x-axis , y-axis , width, hieght)
                    on_button(100,300,'play again?')
                    if click[0] == 1:                                             #the tuple for clicks is (0,0,0) [0] = left click ,[1]= middle click. if clicked [0] or [1] or [2] = 1
                        main_func()

                pygame.draw.rect(screen, red, (500, 300, 200, 50))
                on_button((500 + 50),(300 + 5),"I QUIT")

                if 500+ 200 >mouse[0] > 500 and 300 +50 >mouse[1] > 300:
                    pygame.draw.rect(screen, brigth_red, (500, 300, 200, 50))
                    on_button((500 + 50),(300 + 5),"I QUIT")
                    if click[0] == 1:
                        running = False
                        break

        enemyX[i] += enemyX_change[i]                      #enemy movement
        if enemyX[i] <= 0:                              #(The boundary two and fro movement)
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:                          #(               "                 )
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        coalision = iscoalision(bulletX, bulletY, enemyX[i], enemyY[i])

        if coalision:
            bullet_state = "ready"
            bulletY = 480
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()


    # I WILL GOOGLE ANOTHER FILE WHICH RUNS A PYTHON FILE INTO ANOTHER PYTHON FILE
