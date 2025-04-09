# Katelyn Curtiss
# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_rectangle(screen, x, y, width, height):
    pygame.draw.rect(screen, config.RED, (100,150, 30,30))

def draw_text(screen, text, x,y, font_size, font_color, font_name=None, bold=False, italic=False):
    if font_name:
        font=pygame.font.Font(font_name, font_size)

    else:
        font = pygame.font.Font(None, font_size)

    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, font_color)
    screen.blit(text_surface, (x,y))

def main():

    screen = init_game()
    clock = pygame.time.Clock() 
    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  

        font_x = 200
        font_y = 120
        font_size = 40
        font_color = config.RED
        font_name = None

       
        font_x2 = 200
        font_y2 = 150
        font_size2 = 40
        font_color2 = config.BLUE
        font_name2 = None

        draw_text(screen, "Katelyn Curtiss", font_x, font_y, font_size, font_color, font_name, bold=False, italic=False)

        draw_text(screen, "Career Tech", font_x2, font_y2, font_size2, font_color2, font_name2, bold=False, italic=False)
     
        pygame.display.flip()

        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)



        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()