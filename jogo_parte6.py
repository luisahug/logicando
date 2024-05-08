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
fonte = pygame.font.Font(None, 36) #caract. gráficas do placar do jogo

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
#variáveis de controle da pontuação de cada jogador, inciam zeradas
pontos_jogador1 = 0
pontos_jogador2 = 0

#loop de execução do jogo (cada repetição é um frame)
while executando:
    #se o evento for de fechar a janela, executando se torna False e encerra o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    #eventos que definem o movimento dos jogadores
    tecla = pygame.key.get_pressed() #salva qual tecla do teclado foi apertada
    #jogador 1
    #tecla W (cima)
    if tecla[pygame.K_w] and y_jogador1 >= 5: #verifica se jogador está no limite da tela
        y_jogador1 -=5  #quanto maior o num, mais rápido ele anda
    #tecla S (baixo)                   
    elif tecla[pygame.K_s] and y_jogador1 < altura_tela-altura_jogadores: #verifica se jogador está no limite da tela
        y_jogador1 +=5  #quanto maior o num, mais rápido ele anda
    #jogador 2
    #tecla up/seta para cima (cima)
    if tecla[pygame.K_UP] and y_jogador2 >= 5: #verifica se jogador está no limite da tela
        y_jogador2 -=5  #quanto maior o num, mais rápido ele anda
    #tecla down/seta para baixo (baixo)
    elif tecla[pygame.K_DOWN] and y_jogador2 < altura_tela-altura_jogadores: #verifica se jogador está no limite da tela
        y_jogador2 +=5  #quanto maior o num, mais rápido ele anda

    #iteração (movimento) da bola
    x += vel_x
    y += vel_y
    #verifica se a bola vai encostar no limite da tela e inverte o movimento
    if y <= 0 or y >= altura_tela: vel_y = -vel_y
    
    #posição atual dos elementos na tela
    rect_jogador1 = pygame.Rect(x_jogador1, y_jogador1, largura_jogadores, altura_jogadores)
    rect_jogador2 = pygame.Rect(x_jogador2, y_jogador2, largura_jogadores, altura_jogadores)
    rect_bola = pygame.Rect(x, y, raio_bola, raio_bola)

    #verifica se há colisão entre bola e jogadores
    #ao colidir a bola com o jogador, esse recebe um ponto
    if rect_bola.colliderect(rect_jogador1):
        pontos_jogador1 += 1 
        vel_x = -vel_x
    if rect_bola.colliderect(rect_jogador2):
        pontos_jogador2 += 1
        vel_x = -vel_x
    #verifica se há colisão entre bola e parede lateral
    #ao colidir a bola com uma parede lateral, o placar zera
    #e os jogadores voltam a sua posição inicial
    if x >= largura_tela or x <= 0: 
        pontos_jogador1 = 0 
        pontos_jogador2 = 0
        x = largura_tela/2
        y = altura_tela/2

    #informações placar:
    #trasnforma pontos int em string
    txt_pontos_jogador1 = str(pontos_jogador1)
    txt_pontos_jogador2 = str(pontos_jogador2)
    #concatena pontos e X para exibir no placar
    txt_pontos = fonte.render(txt_pontos_jogador1 + " x " + txt_pontos_jogador2, True, (255,255,255))
    rect_pontos = txt_pontos.get_rect() #encontra posição atual do placar
    rect_pontos.center = (largura_tela // 2, altura_tela // 2) #centraliza placar na tela
    rect_pontos.y = 35 #altura desejada do placar na tela
    
    #exibição dos elementos
    tela.fill((0,0,0)) #cor de fundo da tela
    superficie_bola(tela, (255,255,255), x, y, raio_bola) #exibe a bola
    #exibe cada jogador
    superficie_jogador(tela, (255,0,0), x_jogador1, y_jogador1, largura_jogadores, altura_jogadores)
    superficie_jogador(tela, (0,0,255), x_jogador2, y_jogador2, largura_jogadores, altura_jogadores)
    tela.blit(txt_pontos, rect_pontos) #exibe o placar de pontos
    
    #atualização da tela a cada loop
    pygame.display.flip()
    pygame.time.delay(10)
    #fim do loop
    
#encerra elementos da biblioteca pygame no programa
pygame.quit()