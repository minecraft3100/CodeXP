import pygame
from constantes import *
from game import Game

pygame.init()

pygame.display.set_caption("Jeu 1")
screen = pygame.display.set_mode((RESOLUTION_X,RESOLUTION_Y))

background = pygame.image.load("assets/background.jpg")


game = Game()

running = True

# Boucle de jeu
while running:
    
    screen.blit(background,(0,-130))
    screen.blit(game.player.image, game.player.rect)

    pygame.display.flip()
    
    if game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q):
        game.player.move_left()
    print(game.player.rect.x)

    # Boucle d'events
    for event in pygame.event.get():
        match event.type:
            # Detection quitter la fenetre
            case pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture")
            # Detection touche enfoncé
            case pygame.KEYDOWN:
                game.pressed[event.key] = True
            case pygame.KEYUP:
                game.pressed[event.key] = False