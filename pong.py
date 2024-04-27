import pygame

class Ball:
    def __init__(self, surf, color, radius):
        self.surf = surf
        self.color = color
        self.radius = radius

    def surface(self, x, y):
        pygame.draw.circle(self.surf, self.color, (x,y), self.radius)
    

class Player:
    def __init__(self, surf, color, width, height):
        self.surf = surf
        self.color = color
        self.width = width
        self.height = height

    def surface(self, x, y):
        pygame.draw.rect(self.surf, self.color, (x, y, self.width, self.height))

pygame.init()
screen_width = 800
screen_height = 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping")
running = True

#informações da bola
x = screen_width/2
y = screen_height/2
vel_x = 3
vel_y = 3

ball = Ball(screen, (255,255,255), 10)

#informações dos players
width_players = 8
height_players = 80

x_player1 = 0
y_player1 = 2*screen_height/5

x_player2 = screen_width-width_players
y_player2 = 2*screen_height/5

player1 = Player(screen, (255,255,255), width_players, height_players)
player2 = Player(screen, (255,255,255), width_players, height_players)


while running:
    screen.fill((0,0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #player 1
            if event.key == pygame.K_w and y_player1 >= 20: 
                y_player1 -=20
            elif event.key == pygame.K_s and y_player1 < screen_height-height_players:
                y_player1 +=20
            #player 2
            if event.key == pygame.K_UP and y_player2 >= 20: 
                y_player2 -=20
            elif event.key == pygame.K_DOWN and y_player2 < screen_height-height_players:
                y_player2 +=20

        
    
    x += vel_x
    y += vel_y

    if x <= 0 or x >= screen_width: vel_x = - vel_x
    if y <= 0 or y >= screen_height: vel_y = - vel_y

    ball.surface(x, y)
    player1.surface(x_player1, y_player1)
    player2.surface(x_player2, y_player2)

    pygame.display.flip()
    pygame.time.delay(10)


pygame.quit()

