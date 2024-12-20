import pygame

pygame.init()
displayWidth = 800
displayHeight = 600

#colors; measured in RGB
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight)) #resolution, has to be a tuple    
pygame.display.set_caption('A Bit Racey') #window title

clock = pygame.time.Clock()

gyarImg = pygame.image.load('gyarados.xcf') #loading image

def gyar(x, y):
    #blit is showing; (x,y) HAS to be a tuple
    gameDisplay.blit(gyarImg, (x, y))

x = (displayWidth  * 0.45)
y = (displayHeight * 0.6 )

crash = False

while not crash:

    for event in pygame.event.get(): # gets event: where's the mouse, are they clicking, what are they clicking
        if event.type == pygame.QUIT: 
            crash = True
        
        print(event)
    
    gameDisplay.fill(white) # this first so the object isn't painted over
    gyar(x, y)
    pygame.display.update() #display.flip updates the entire surface
                            #.update can do specific areas or entire surface if you don't include a param
    clock.tick(60)

pygame.quit()
quit()