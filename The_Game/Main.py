import pygame
import math

# X MUST BE LARGER THAN Y
# use these to scale the buttons with the screen
x_size = 1200
y_size = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode((x_size, y_size))

    pygame.display.set_caption("Sign Language Recognition Game")

    alphabet = ['K_a', 'K_b', 'K_c',
                'K_d', 'K_e', 'K_f',
                'K_g', 'K_h', 'K_i',
                'K_j', 'K_k', 'K_l',
                'K_m', 'K_n', 'K_o',
                'K_p', 'K_q', 'K_r',
                'K_s', 'K_t', 'K_u',
                'K_v', 'K_w', 'K_x',
                'K_y', 'K_z']

    # use this for scaling button distances
    scale = math.floor((x_size / y_size) * 3)

    # forest green = 0
    # light purple = 1
    # aqua blue = 2
    colors = [(105, 149, 0), (141, 91, 112), (0, 59, 86)]

    running = True
    while running:
        # insert if needed for the future
        clock = pygame.time.Clock()

        for event in pygame.event.get():

            buttons = button_make()
            color_count = len(colors) - 1
            for x in buttons:
                pygame.draw.rect(screen, colors[color_count], x, scale)
                color_count -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in buttons:
                    if x.collidepoint(event.pos):
                        if x is buttons[0]:
                            print("in game")
                            game_screen()
                        elif x is buttons[1]:
                            print("in controls")
                            controls()
                        elif x is buttons[2]:
                            print("in about")
                            about()

            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()

    pygame.quit()


# make the buttons for the main screen
def button_make():
    # draw on screen, color, place, and make just outline fill
    button1 = pygame.Rect((math.floor(x_size * 0.3), math.floor(y_size * 0.25),
                           (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                           (math.floor(y_size * 0.35) - math.floor(y_size * 0.25))))

    button2 = pygame.Rect((math.floor(x_size * 0.3), math.floor(y_size * 0.55),
                           (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                           (math.floor(y_size * 0.65) - math.floor(y_size * 0.55))))

    button3 = pygame.Rect((math.floor(x_size * 0.3), math.floor(y_size * 0.85),
                           (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                           (math.floor(y_size * 0.95) - math.floor(y_size * 0.85))))

    buttons = [button1, button2, button3]

    return buttons


def game_screen():
    return


def controls():
    return


def about():
    return


if __name__ == "__main__":
    # call the main function
    main()
