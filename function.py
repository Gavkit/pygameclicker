import pygame

coins = 0

res = (1000, 500)
screen = pygame.display.set_mode(res)
screen.fill("black")
pygame.display.set_caption('Nova Clicker')

clock = pygame.time.Clock()
player_mouse_pos = pygame.mouse.get_pos()


def createScreen():
    screen.fill("black")


def init():
    global res
    global coins
    global screen
    global clock
    global player_mouse_pos
    global coinAmount
    createScreen()


def DrawText(text, textcolor, rectcolor, x, y, fsize, ftype):
    font = get_font(fsize, ftype)
    text = font.render(text, True, textcolor, rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def get_font(size, types):
    if types == 1:
        return pygame.font.Font("font/roboto.ttf", size)
    else:
        return pygame.font.Font("font/roboto.ttf", size)


def update():
    pygame.display.update()
    clock.tick(60)
