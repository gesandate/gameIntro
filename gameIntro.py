import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A Bit Racey')

clock = pygame.time.Clock()

crash = False


while not crash:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        
        print(event)
    
    pygame.display.update() #display.flip updates the entire surface
                            #.update can do specific areas if you don't include a param
    clock.tick(60)

pygame.quit()
quit()