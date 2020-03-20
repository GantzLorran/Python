import pygame
from random import randrange
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    pygame.init()
except:
    print('\033[31mNão foi possível iniciar o game')
largura = 400
altura = 500
tamanho=10
placar = 40
pontos = 0
pos_x=largura/2
pos_y=altura/2
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")
#Tela de Game Over

def texto(msg, cor, tam,x,y):#centralizar o texto na tela
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x,y])
#Tela de Game Over
def cobra(CobraXY):#Essa função define a cobra
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, (XY[0], XY[1], tamanho, tamanho))
def maca(maca_x, maca_y):#Essa função define os pontinhos vermelhos que precisam pegar para aumentar a cobra
    pygame.draw.rect(fundo, vermelho, (maca_x, maca_y, tamanho, tamanho))
def jogo():
    sair = True
    fimdejogo = False
    pos_x=randrange(0,largura-tamanho,10)
    pos_y=randrange(0,altura-tamanho-placar,10)
    maca_x = randrange(0, largura - tamanho, 10)
    maca_y = randrange(0, altura - tamanho-placar, 10)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []  # Função que aumenta a cobra
    cobraComp = 1
    pontos = 0
    while sair:
        while fimdejogo:
            for event in pygame.event.get():  # Comandos para fazer movimentação da cobra
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho-placar, 10)
                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho-placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []  # Função que aumenta a cobra
                        cobraComp = 1
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print(pygame.mouse.get_pos())
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho - placar, 10)
                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho - placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []  # Função que aumenta a cobra
                        cobraComp = 1
                        pontos = 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair = True
                        fimdejogo = False
                fundo.fill(branco)
                texto("Fim de jogo", vermelho, 50,65,30)
                texto("Pontuação final: " +str(pontos),preto,30,70,80)
                pygame.draw.rect(fundo, preto,[45,120,135,27])
                texto("Continuar(c)", branco, 30,50,125)
                pygame.draw.rect(fundo, preto, [190,120,75,27])
                texto("Sair(s) ",branco,30,195,125)
                pygame.display.update()
        for event in pygame.event.get():#Comandos para fazer movimentação da cobra
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho
            print(event)
        fundo.fill(branco)


        CobraInicio = []
        CobraInicio.append(pos_x)#pega o valor 1
        CobraInicio.append(pos_y)#pega o valor 2
        CobraXY.append(CobraInicio)
        cobra(CobraXY)
        if len(CobraXY) > cobraComp:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True
        if pos_x == maca_x and pos_y == maca_y:#Função para a cobra comer a maçã
            maca_x = randrange(0, largura - tamanho, 10)
            maca_y = randrange(0, altura - tamanho-placar, 10)
            cobraComp += 1
            pontos+=1
        pygame.draw.rect(fundo, preto, (pos_x, pos_y,tamanho,tamanho))
        pos_x+=velocidade_x
        pos_y+=velocidade_y
        maca(maca_x,maca_y)
        pygame.display.update()
        relogio.tick(10)
        if pos_x + tamanho > largura:
            pos_x = 0
            #fimdejogo = True#Isso aqui é se caso a cobra bater nos cantos da tela
        if pos_x < 0:
            pos_x = largura - tamanho
            # fimdejogo = True
        if pos_y + tamanho > altura-placar:
            pos_y = 0
            # fimdejogo = True
        if pos_y < 0:
            pos_y = altura - tamanho - placar
            #fimdejogo = True
        '''if pos_x > largura:
            fimdejogo = True#Isso aqui é se caso a cobra bater nos cantos da tela
        if pos_x < 0:
            fimdejogo = True
        if pos_y > altura:
            fimdejogo = True
        if pos_y < 0:
            fimdejogo = True'''
    #pos_x+=0.2#Define a velocidade da cobra
    # Desenhando a barra de score
    pygame.draw.rect(fundo, preto, (0, altura-placar, largura, placar))
    # Desenhando a barra de score
    texto("Pontuação: "+str(pontos), vermelho, 20, 10, altura-30)
    cobra(CobraXY)
jogo()
pygame.quit()