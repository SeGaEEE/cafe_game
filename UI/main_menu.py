import pygame
import sys
from pygame_button import Button
pygame.font.init()



FPS = 60
WIN_WIDTH = 200
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

r = 30
# координаты круга
# скрываем за левой границей
x = 0 + r
# выравнивание по центру по вертикали
y = WIN_HEIGHT // 2


# buttons:
START_button = pygame.Rect((50, 210, 100, 40))
QUIT_button = pygame.Rect((50, 270, 100, 40))

b1 = Button(START_button, WHITE, None)
b1.text = 'starrrt'



font = pygame.font.Font(None, 36)
text1 = font.render("Start", True, (0, 100, 200))
place1 = text1.get_rect(center=(100, 230))


text2 = font.render("Exit", True, (100, 20, 0))
place2 = text1.get_rect(center=(100, 290))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            if 50 < pos[0] < 150 and 210 < pos[1] < 250:
                print('started')
            if 50 < pos[0] < 150 and 270 < pos[1] < 310:
                sys.exit()
    sc.fill(ORANGE)
    pygame.draw.rect(sc, WHITE, START_button)
    sc.blit(text1, place1)
    pygame.draw.rect(sc, WHITE, QUIT_button)
    sc.blit(text2, place2)
    pygame.display.update()

    clock.tick(FPS)