import pygame

#definição das funções de exibição dos elementos móveis 
def superficie_bola(surf, cor, x,y, raio):
    pygame.draw.circle(surf, cor, (x,y), raio)

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
raio_bola = 10

#loop de execução do jogo (cada repetição é um frame)
while executando:
    #se o evento for de fechar a janela, executando se torna False e encerra o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
    
    
    #exibição dos elementos
    tela.fill((0,0,0)) #cor de fundo da tela
    superficie_bola(tela, (255,255,255), x, y, raio_bola) #exibe a bola
   
    #atualização da tela a cada loop
    pygame.display.flip()
    pygame.time.delay(10)
    #fim do loop
    
#encerra elementos da biblioteca pygame no programa
pygame.quit()