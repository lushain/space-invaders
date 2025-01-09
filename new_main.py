import pygame                                             # Type 'pip install pygame in the cammand promt'
import random                                             # Type 'pip install random in the cammand promt'
import math


class Commands():

    def __init__(self):
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

        over_text = pygame.font.Font('freesansbold.ttf',128)
        running = True

        def player(self, x, y):
            screen.blit(player_icon,(x, y))

        def enemy(self, x, y, i):
            screen.blit(enemy_icon[i], (x, y))

        def show_score(self, x,y):
            score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
            screen.blit(score, (x, y))

        def game_over_text(self):
            over_text = font.render('GAME OVER !!' , True, (255, 255, 255))
            screen.blit(over_text, (300, 150))

        def on_button(self, x,y,text =''):
            font = pygame.font.Font('freesansbold.ttf', 5)
            button_text = font.render(text, True, (black))
            screen.blit(button_text, ((x + 5), (y + 5)))


        def bullet(self, x, y):
            screen.blit(bullet_icon, (x, y))             # Function to display enemy_icon {there is supposed to be a comma after image name}

        def fire_bullet(self, x,y):
            global bullet_state
            bullet_state = "fire"
            screen.blit(bullet_icon, (x+19, y+10))

        def iscoalision(self, bulletX,bulletY,enemyX,enemyY):
            distance = math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY-bulletY,2))
            if distance < 25:
                return True
            else:
                return
