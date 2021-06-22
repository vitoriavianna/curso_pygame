import pygame
from pygame.locals import (DOUBLEBUF,
                           FULLSCREEN,
                           KEYDOWN,
                           KEYUP,
                           K_LEFT,
                           K_RIGHT,
                           QUIT,
                           K_ESCAPE,
                           K_SPACE
                           )
from fundo import Fundo
from elementos import ElementoSprite
import random

nivel = 1
class Jogo:
    def __init__(self, size=(800, 800), fullscreen=False):
        self.elementos = {}
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.fundo = Fundo()
        flags = DOUBLEBUF
        if fullscreen:
            flags |= FULLSCREEN

        self.screen_size = self.screen.get_size()
        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Corona Shooter')
        self.run = True

    def atualiza_elementos(self, dt):
        self.fundo.update(dt)

    def desenha_elementos(self):
        self.fundo.draw(self.screen)
        self.nave.draw(self.screen)
        
        if nivel>0:
            for el in self.elementos['virii']:
                el.draw(self.screen)
        if nivel>1: 
            for el in self.elementos['virii2']:
                el.draw(self.screen)
        if nivel>2:
            for el in self.elementos['virii3']:
                el.draw(self.screen)  

    def trata_eventos(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False

        if event.type in (KEYDOWN, KEYUP):
            key = event.key
            if key == K_ESCAPE:
                self.run = False
        # ESPAÇO ATIRA
            if key == K_SPACE:
                self.interval = 0
                self.jogador.atira(self.elementos["tiros"])

    def loop(self):
        clock = pygame.time.Clock()
        if nivel > 0:
            dt = 4
        else:
            dt = 16
        # desenhar o virus na tela
        #self.elementos['virii'] = [pygame.sprite.RenderPlain(Virus([120, 50]))]
        #self.elementos['virii2'] = [pygame.sprite.RenderPlain(Virus2([500, 70]))]
        #self.elementos['virii3'] = [pygame.sprite.RenderPlain(Virus3([300, 300]))]
        
        # implementar logica de nivel 
           
        if nivel == 1: 
            self.elementos['virii'] = [pygame.sprite.RenderPlain(Virus([120, 50]))]
        if nivel == 2: 
            self.elementos['virii'] = [pygame.sprite.RenderPlain(Virus([120, 50]))]
            self.elementos['virii2'] = [pygame.sprite.RenderPlain(Virus2([500, 70]))]
        if nivel == 3:
            self.elementos['virii'] = [pygame.sprite.RenderPlain(Virus([120, 50]))]
            self.elementos['virii2'] = [pygame.sprite.RenderPlain(Virus2([500, 70]))]
            self.elementos['virii3'] = [pygame.sprite.RenderPlain(Virus3([300, 300]))]

        self.nave = pygame.sprite.RenderPlain(Nave([200, 400], 5))
        while self.run:
            clock.tick(1000 / dt)

            self.trata_eventos()

            # Atualiza Elementos
            self.atualiza_elementos(dt)

            # Desenhe no back buffer
            self.desenha_elementos()
            pygame.display.flip()

class Nave(ElementoSprite):
    def __init__(self, position, lives=0, speed=[0, 0], image=None, new_size=[83, 248]):
        self.acceleration = [3, 3]
        if not image:
            image = "seringa.png"
        super().__init__(image, position, speed, new_size)
        self.set_lives(lives)

    def get_lives(self):
        return self.lives

    def set_lives(self, lives):
        self.lives = lives
        
        #ATIRAR
    def atira(self, lista_de_tiros, image=None):
        s = list(self.get_speed())
        s[1] *= 2
        Tiro(self.get_pos(), s, image, lista_de_tiros)

#defini o virus 1 com 1 vida
class Virus(Nave):
    def __init__(self, position, lives=0, speed=None, image=None, size=(100, 100)):
        if not image:
            image = "virus.png"
        super().__init__(position, lives, speed, image, size)
        
#defini o virus 2 com 2 vidas
class Virus2(Nave):
    def __init__(self, position, lives=2, speed=None, image=None, size=(100, 100)):
        if not image:
            image = "virus2.png"
        super().__init__(position, lives, speed, image, size)
        
#defini o virus 3 com 3 vidas
class Virus3(Nave):
    def __init__(self, position, lives=3, speed=None, image=None, size=(100, 100)):
        if not image:
            image = "virus3.png"
        super().__init__(position, lives, speed, image, size)
        

class Tiro(ElementoSprite):
    def __init__(self, position, speed=None, image=None, list=None):
        if not image:
            image = "tiro.png"
        super().__init__(image, position, speed)
        if list is not None:
            self.add(list)
            
            

if __name__ == '__main__':
    J = Jogo()
    J.loop()