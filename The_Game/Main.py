import pygame
import math


def main():
    # X MUST BE LARGER THAN Y
    # use these to scale the buttons with the screen
    x_size = 1200
    y_size = 800

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

    # red = 0
    # green = 1
    # blue = 2
    # light purple = 3
    # aqua blue = 4
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (141, 91, 112), (0, 59, 86)]

    running = True
    while running:
        for event in pygame.event.get():

            # draw on screen, color, place, and make just outline fill
            pygame.draw.rect(screen, colors[4], (math.floor(x_size * 0.3), math.floor(y_size * 0.15),
                                                 (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                                                 (math.floor(y_size * 0.25) - math.floor(y_size * 0.15))),
                             scale)

            pygame.draw.rect(screen, colors[3], (math.floor(x_size * 0.3), math.floor(y_size * 0.45),
                                                 (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                                                 (math.floor(y_size * 0.55) - math.floor(y_size * 0.45))),
                             scale)

            pygame.draw.rect(screen, colors[0], (math.floor(x_size * 0.3), math.floor(y_size * 0.75),
                                                 (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                                                 (math.floor(y_size * 0.85) - math.floor(y_size * 0.75))),
                             scale)

            pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    # call the main function
    main()
