import pygame
import weathericons

pygame.init()
screen = pygame.display.set_mode((320,240))
pygame.display.set_caption('Nightstand')

background = pygame.Surface(screen.get_size()).convert()
background.fill((0,0,0))

def blitBase():
	screen.blit(background, (0,0))
	screen.fill(Color(255,255,255,255), (0,175,320,180))
	screen.blit(ToolbarIcons.Time, (20,190))
	screen.blit(ToolbarIcons.Weather, (100,190))
	screen.blit(ToolbarIcons.Pollen, (180,190))
	screen.blit(ToolbarIcons.SunIntensity, (260, 190))

blitBase()
pygame.display.flip()

clock = pygame.time.Clock()
while not pygame.QUIT in [e.type for e in pygame.event.get()]:
	clock.tick(15)
