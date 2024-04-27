import pygame

class Ball:
    def __init__(self, surf, color, radius):
        self.surf = surf
        self.color = color
        self.radius = radius

    def surface(self, x, y):
        pygame.draw.circle(self.surf, self.color, (x,y), self.radius)
    

class Player:
    def __init__(self, surf, color, x, y, width, height):
        self.surf = surf
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def surface(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, self.width, self.height))

pygame.init()
screen_width = 800
screen_height = 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping")
running = True

#informações da bola
x = screen_width/2
y = screen_height/2
vel_x = 5
vel_y = 5

ball = Ball(screen, (255,255,255), 10)

#informações dos players
width_players = 8
height_players = 80

x_player1 = 0
y_player1 = 2*screen_height/5

x_player2 = screen_width-width_players
y_player2 = 2*screen_height/5

player1 = Player(screen, (255,255,255),x_player1, y_player1, width_players, height_players)
player2 = Player(screen, (255,255,255), x_player2, y_player2, width_players, height_players)


while running:
    screen.fill((0,0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    x += vel_x
    y += vel_y

    if x <= 0 or x >= screen_width: vel_x = - vel_x
    if y <= 0 or y >= screen_height: vel_y = - vel_y

    ball.surface(x, y)
    player1.surface()
    player2.surface()

    pygame.display.flip()
    pygame.time.delay(10)


pygame.quit()

