import pygame

''''class Ball:
    def __init__(self, surf, color, radius):
        self.surf = surf
        self.color = color
        self.radius = radius

    def surface(self, x, y):
        pygame.draw.circle(self.surf, self.color, (x,y), self.radius)'''''
    
def surface_bola(surf, cor, x,y, raio):
    pygame.draw.circle(surf, cor, (x,y), raio)

class Player:
    def __init__(self, surf, color, width, height):
        self.surf = surf
        self.color = color
        self.width = width
        self.height = height

    def surface(self, x, y):
        pygame.draw.rect(self.surf, self.color, (x, y, self.width, self.height))

pygame.init()
largura_tela = 800
altura_tela = 350
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Ping")
running = True

#informações da bola
x = largura_tela/2
y = altura_tela/2
vel_x = 3
vel_y = 3
raio_bola = 10
#bola = Ball(tela, (255,255,255), 10)

#informações dos players
largura_jogadores = 8
altura_jogadores = 80

x_jogador1 = 0
y_jogador1 = 2*altura_tela/5

x_jogador2 = largura_tela-largura_jogadores
y_jogador2 = 2*altura_tela/5

jogador1 = Player(tela, (255,255,255), largura_jogadores, altura_jogadores)
jogador2 = Player(tela, (255,255,255), largura_jogadores, altura_jogadores)

pontos_jogador1 = 0
pontos_jogador2 = 0


#informações placar de pontos
fonte = pygame.font.Font(None, 36)


while running:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #movimento dos players
    tecla = pygame.key.get_pressed()
    #player 1
    if tecla[pygame.K_w] and y_jogador1 >= 5: 
        y_jogador1 -=5
    elif tecla[pygame.K_s] and y_jogador1 < altura_tela-altura_jogadores:
        y_jogador1 +=5
    #player 2
    if tecla[pygame.K_UP] and y_jogador2 >= 5: 
        y_jogador2 -=5
    elif tecla[pygame.K_DOWN] and y_jogador2 < altura_tela-altura_jogadores:
        y_jogador2 +=5
    #iteração da bola
    x += vel_x
    y += vel_y
    if y <= 0 or y >= altura_tela: vel_y = -vel_y
    
    #colisões bola X players
    txt_pontos_jogador1 = str(pontos_jogador1)
    txt_pontos_jogador2 = str(pontos_jogador2)
    rect_jogador1 = pygame.Rect(x_jogador1, y_jogador1, jogador1.width, jogador1.height)
    rect_jogador2 = pygame.Rect(x_jogador2, y_jogador2, jogador2.width, jogador2.height)
    rect_bola = pygame.Rect(x, y, raio_bola, raio_bola)

    if rect_bola.colliderect(rect_jogador1):
        pontos_jogador1 += 1
        vel_x = -vel_x
    if rect_bola.colliderect(rect_jogador2):
        pontos_jogador2 += 1
        vel_x = -vel_x
    #colisões bola X parede
    if x >= largura_tela or x <= 0: 
        pontos_jogador1 = 0 
        pontos_jogador2 = 0
        x = largura_tela/2
        y = altura_tela/2

    #informações placar:
    txt_pontos = fonte.render(txt_pontos_jogador1 + " x " + txt_pontos_jogador2, True, (255,255,255))
    rect_pontos = txt_pontos.get_rect()
    rect_pontos.center = (largura_tela // 2, altura_tela // 2)
    rect_pontos.y = 35
    
    #exibição dos elementos
    #bola.surface(x, y)
    surface_bola(tela, (255,255,255), x, y, raio_bola)
    jogador1.surface(x_jogador1, y_jogador1)
    jogador2.surface(x_jogador2, y_jogador2)
    tela.blit(txt_pontos, rect_pontos)
    
    #atualização da tela a cada loop
    pygame.display.flip()
    pygame.time.delay(10)


pygame.quit()