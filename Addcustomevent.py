import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Colour Change Event")
WHITE = (255, 255, 255)
COLOURS = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
           (255, 255, 0), (255, 0, 255), (0, 255, 255)]
CHANGE_COLOUR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOUR_EVENT, 2000)
class ColourSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, colour):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.colour = colour
    def change_colour(self):
        self.colour = random.choice(COLOURS)
        self.image.fill(self.colour)
sprite1 = ColourSprite(200, HEIGHT // 2, random.choice(COLOURS))
sprite2 = ColourSprite(400, HEIGHT // 2, random.choice(COLOURS))
all_sprites = pygame.sprite.Group(sprite1, sprite2)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOUR_EVENT:
            sprite1.change_colour()
            sprite2.change_colour()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()