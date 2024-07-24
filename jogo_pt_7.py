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

#variável de controle da pausa do jogo
pausa = False

#loop de execução do jogo (cada repetição é um frame)
while executando:
    #se o evento for de fechar a janela, executando se torna False e encerra o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
    
        #tecla R reinicia o jogo
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    #reinicia o jogo
                    pontos_jogador1 = 0
                    pontos_jogador2 = 0
                    vencedor = ""
                    pausa = False
                    #reposiciona a bola no centro
                    x = largura_tela / 2
                    y = altura_tela / 2


    if not pausa:  #enquanto o jogo estiver funcionando
        #eventos que definem o movimento dos jogadores
        tecla = pygame.key.get_pressed() #salva qual tecla do teclado foi apertada
        #jogador 1
        #tecla W (cima)
        if tecla[pygame.K_w] and y_jogador1 >= 5: #verifica se jogador está no limite da tela
            y_jogador1 -=10                        #sendo 5 
        elif tecla[pygame.K_s] and y_jogador1 < altura_tela-altura_jogadores: #verifica se jogador está no limite da tela
            y_jogador1 +=5
        #jogador 2
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
        rect_jogador1 = pygame.Rect(x_jogador1, y_jogador1, largura_jogadores, altura_jogadores)
        rect_jogador2 = pygame.Rect(x_jogador2, y_jogador2, largura_jogadores, altura_jogadores)
        rect_bola = pygame.Rect(x, y, raio_bola, raio_bola)

        if rect_bola.colliderect(rect_jogador1):
            pontos_jogador1 += 1
            vel_x = -vel_x
        if rect_bola.colliderect(rect_jogador2):
            pontos_jogador2 += 1
            vel_x = -vel_x
        #colisões bola X parede
        if x >= largura_tela: #or x <= 0: 
            #pontos_jogador1 = 0 
            pontos_jogador2 = 0
            x = largura_tela/2
            y = altura_tela/2
        if x <= 0: #or x <= 0: 
            pontos_jogador1 = 0 
            #pontos_jogador2 = 0
            x = largura_tela/2
            y = altura_tela/2

    
        #verifica o vencedor e pausa o jogo
        vencedor = ""
        if (pontos_jogador1) >= 3: 
            txt_pontos_jogador1 = "3" #hack pois se não ele exibe o valor anterior de ganhar
            #altera o texto de vitória
            vencedor = "Jogador vermelho ganhou o jogo!"
            #pausa o jogo, para a bolinha e os movimentos dos players
            pausa = True

        if (pontos_jogador2) >= 3: 
            txt_pontos_jogador2 = "3"
            vencedor = "Jogador azul ganhou o jogo!"
            pausa = True


    #informações placar:
    txt_pontos = fonte.render(txt_pontos_jogador1 + " x " + txt_pontos_jogador2, True, (255,255,255))
    rect_pontos = txt_pontos.get_rect()
    rect_pontos.center = (largura_tela // 2, altura_tela // 2)
    rect_pontos.y = 35

    #exibição dos elementos
    tela.fill((0,0,0)) #cor de fundo da tela
    bola = superficie_bola(tela, (255,255,255), x, y, raio_bola) #exibe a bola
    #exibe cada jogador
    jogador1 = superficie_jogador(tela, (255,0,0), x_jogador1, y_jogador1, largura_jogadores, altura_jogadores)
    jogador2 = superficie_jogador(tela, (0,0,255), x_jogador2, y_jogador2, largura_jogadores, altura_jogadores)
    tela.blit(txt_pontos, rect_pontos) #exibe o placar de pontos
        

    #exibe na tela o nome do jogador quando um vencer
    txt_vencedor = fonte.render(vencedor, True, (255,255,255))
    rect_vencedor = txt_vencedor.get_rect()
    rect_vencedor.center = (largura_tela // 2, altura_tela // 2)
    tela.blit(txt_vencedor, rect_vencedor)

    #exibe a mensagem de reiniciar quando o jogo finalizar
    if vencedor != "":
        txt_reiniciar = fonte.render("Clique em R para recomeçar o jogo.", True, (255,255,255))
        rect_reiniciar = txt_reiniciar.get_rect()
        rect_reiniciar.center = (largura_tela// 2, altura_tela//2 + 35)
        tela.blit(txt_reiniciar, rect_reiniciar)
    
    #atualização da tela a cada loop
    pygame.display.flip()
    pygame.time.delay(10)


pygame.quit()
