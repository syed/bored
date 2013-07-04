import pygame,sys
from pygame.locals import *



def toggle_fullscreen():

    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)
 
    pygame.key.set_mods(0) 
 
    pygame.mouse.set_cursor( *cursor )  
    
    return screen
 
def main():

    pygame.init()
    display_surface = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Hello World!")
    RED = (255,0,0)
    cur_x, cur_y = 0,0
    prev_x, prev_y = 0,0

    mouseClicked = False
    while True:

        for event in pygame.event.get():
            print event.type
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                prev_x, prev_y = cur_x, cur_y
                cur_x, cur_y = event.pos

            elif event.type == MOUSEBUTTONDOWN:
                prev_x, prev_y = cur_x, cur_y
                cur_x, cur_y = event.pos
                mouseClicked = True
            elif event.type == MOUSEBUTTONUP:
                prev_x, prev_y = cur_x, cur_y
                cur_x, cur_y = event.pos
                mouseClicked = False
            elif (event.type ==  KEYDOWN and event.key == K_RETURN
                    and (event.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                toggle_fullscreen()

            if mouseClicked:
                pygame.draw.line(display_surface,
                                 RED,
                                 (prev_x, prev_y),
                                 (cur_x , cur_y),
                                 4)

        pygame.display.update()

if __name__ == "__main__":
    main() 
