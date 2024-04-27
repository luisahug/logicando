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

points_player1 = 0
points_player2 = 0

#informações placar de pontos
font = pygame.font.Font(None, 36)
text_score = font.render(" x " , True, (255,255,255))
rect_score = text_score.get_rect()
rect_score.center = (screen_width // 2, screen_height // 2)
rect_score.y = 35

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #movimento dos players
    keys = pygame.key.get_pressed()
    #player 1
    if keys[pygame.K_w] and y_player1 >= 5: 
        y_player1 -=5
    elif keys[pygame.K_s] and y_player1 < screen_height-height_players:
        y_player1 +=5
    #player 2
    if keys[pygame.K_UP] and y_player2 >= 5: 
        y_player2 -=5
    elif keys[pygame.K_DOWN] and y_player2 < screen_height-height_players:
        y_player2 +=5
    #iteração da bola
    x += vel_x
    y += vel_y
    
    """colisões bola X players
    rect_player1 = pygame.Rect(x_player1, y_player2, player1.width, player1.height)
    rect_player2 = pygame.Rect(x_player2, y_player2, player2.width, player2.height)
    rect_ball = pygame.Rect(x, y, ball.radius, ball.radius)
    if rect_ball.collidepoint(x_player1, y_player1):
        points_player1 += 1
        vel_x = -vel_x
    if rect_ball.collidepoint(x_player2, y_player2):
        points_player2 += 1
        vel_x = -vel_x
    if x <= 0 or x >= screen_width: 

    if y <= 0 or y >= screen_height: 
"""
    #exibição dos elementos
    ball.surface(x, y)
    player1.surface(x_player1, y_player1)
    player2.surface(x_player2, y_player2)
    screen.blit(text_score, rect_score)
    #atualização da tela a cada loop
    pygame.display.flip()
    pygame.time.delay(10)


pygame.quit()

