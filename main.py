import pygame 


pygame.init()
window = pygame.display.set_mode((150,150))


def run():
    game = True


    while game:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False



run()