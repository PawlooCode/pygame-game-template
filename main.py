import pygame
import sys
screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Game Template")
pygame.init()
Red = (255,0,0)
Green = (155,255,155)
width = 64
height = 64
x = 20
y = 634
xtext2 = 80
x_grass = 0
y_grass = 694
height_grass = 40
width_grass = 1280
clock = pygame.time.Clock()
FPS = 60  #ticking fps
blue = (0,90,235)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Game Template v0.1', True, Red, blue)
text2 = font.render("by pawlo", True, Red, blue)
textRect2 = text2.get_rect()
text3 = font.render('press "escape" to leave', True, Red, blue)
textRect = text.get_rect()
textRect3 = text.get_rect()
runningloop = True
while runningloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningloop = False
            pygame.quit() 
    screen.fill((blue))  
    textRect2.center = (1200, 20)
    textRect3.center = (600, 20)
    textRect.center = (160, 20)
    pygame.draw.rect(screen,Red,pygame.Rect(x, y, width, height))  
    pygame.draw.rect(screen,Green,pygame.Rect(x_grass, y_grass, width_grass, height_grass))  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        runningloop = False
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += 4
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= 4   
    if x >= 1220:
        x = 1220
    if x <= 0:
        x = 0
    #print(x)              
    screen.blit(text, textRect)    
    screen.blit(text2, textRect2) 
    screen.blit(text3, textRect3) 
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.update()    
