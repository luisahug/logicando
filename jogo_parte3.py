import pygame

#definição das funções de exibição dos elementos móveis 
def superficie_bola(surf, cor, x,y, raio):
    pygame.draw.circle(surf, cor, (x,y), raio)
def superficie_jogador(surf, cor, x_jogador, y_jogador, largura_jogadores, altura_jogadores):
    pygame.draw.rect(surf, cor, (x_jogador, y_jogador,largura_jogadores, altura_jogadores))

#inicializar os recursos da biblioteca Pygame
pygame.init()

#definição das características fixas da tela
largura_tela = 800
altura_tela = 350
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Ping") #nome da janela do jogo
executando = True #variável de controle do loop principal

#informações da bola
#coordenadas da bola
x = largura_tela/2
y = altura_tela/2
#velocidade dos vetores da bola
vel_x = 3
vel_y = 3
raio_bola = 10

#informações dos jogadores
largura_jogadores = 8
altura_jogadores = 80
#coordenadas do jogador 1
x_jogador1 = 0
y_jogador1 = 2*altura_tela/5  #centraliza ele na lateral da tela
#coordenadas do jogador 2
x_jogador2 = largura_tela-largura_jogadores
y_jogador2 = 2*altura_tela/5  #centraliza ele na lateral da tela

#loop de execução do jogo (cada repetição é um frame)
while executando:
    #se o evento for de fechar a janela, executando se torna False e encerra o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    #iteração (movimento) da bola
    x += vel_x
    y += vel_y
    #verifica se a bola vai encostar no limite da tela e inverte o movimento
    if y <= 0 or y >= altura_tela: vel_y = -vel_y

    if x >= largura_tela or x <= 0: vel_x = -vel_x
    
    #exibição dos elementos
    tela.fill((0,0,0)) #cor de fundo da tela
    superficie_bola(tela, (255,255,255), x, y, raio_bola) #exibe a bola
    #exibe cada jogador
    superficie_jogador(tela, (255,0,0), x_jogador1, y_jogador1, largura_jogadores, altura_jogadores)
    superficie_jogador(tela, (0,0,255), x_jogador2, y_jogador2, largura_jogadores, altura_jogadores)
    
    #atualização da tela a cada loop
    pygame.display.flip()
    pygame.time.delay(10)
    #fim do loop
    
#encerra elementos da biblioteca pygame no programa
pygame.quit()