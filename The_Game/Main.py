import pygame
import math

import os
#import cv2
#from lib import video_processor
#from classifiers import prediction_driver

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#cap = cv2.VideoCapture(0)
pygame.init()

# X MUST BE LARGER THAN Y
# use these to scale the buttons with the screen
#x_size = 1200
#y_size = 800
x_size = 800
y_size = 600
clock = pygame.time.Clock() 
v = 0

screen = pygame.display.set_mode((x_size, y_size))

pygame.display.set_caption("Sign Language Recognition Game")

alphabet = ['pygame.K_a', 'pygame.K_b', 'pygame.K_c',
            'pygame.K_d', 'pygame.K_e', 'pygame.K_f',
            'pygame.K_g', 'pygame.K_h', 'pygame.K_i',
            'pygame.K_j', 'pygame.K_k', 'pygame.K_l',
            'pygame.K_m', 'pygame.K_n', 'pygame.K_o',
            'pygame.K_p', 'pygame.K_q', 'pygame.K_r',
            'pygame.K_s', 'pygame.K_t', 'pygame.K_u',
            'pygame.K_v', 'pygame.K_w', 'pygame.K_x',
            'pygame.K_y', 'pygame.K_z']

value_dict = {'pygame.K_a': 'a', 'pygame.K_b': 'b', 'pygame.K_c': 'c',
              'pygame.K_d': 'd', 'pygame.K_e': 'e', 'pygame.K_f': 'f',
              'pygame.K_g': 'g', 'pygame.K_h': 'h', 'pygame.K_i': 'i',
              'pygame.K_j': 'j', 'pygame.K_k': 'k', 'pygame.K_l': 'l',
              'pygame.K_m': 'm', 'pygame.K_n': 'n', 'pygame.K_o': 'o',
              'pygame.K_p': 'p', 'pygame.K_q': 'q', 'pygame.K_r': 'r',
              'pygame.K_s': 's', 'pygame.K_t': 't', 'pygame.K_u': 'u',
              'pygame.K_v': 'v', 'pygame.K_w': 'w', 'pygame.K_x': 'x',
              'pygame.K_y': 'y', 'pygame.K_z': 'z'}


left_hand_global = False
right_hand_global = False


def increment():
    global v
    v += 1


def main():
    button_words = ['About', 'Controls', 'Play']

    # use this for scaling button distances
    scale = math.floor((x_size / y_size) * 3)

    # forest green = 0
    # light purple = 1
    # aqua blue = 2
    colors = [(105, 149, 0), (141, 91, 112), (0, 59, 86)]

    running = True
    while running:
        # insert if needed for the future
        clock.tick(120)
        buttons = button_make()
        color_count = len(colors) - 1

        for x in buttons:
            pygame.draw.rect(screen, colors[color_count], x, scale)
            color_count -= 1

        word_count = len(button_words) - 1

        for x in buttons:
            text = pygame.font.Font("freesansbold.ttf", math.floor(x.height / 2))
            text_s, text_r = text_objects(button_words[word_count], text)
            text_r.center = (x.centerx, x.centery)
            screen.blit(text_s, text_r)
            word_count -= 1

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in buttons:
                    if x.collidepoint(event.pos):
                        if x is buttons[0]:
                            hand_choice_screen()
                            game_screen()
                            screen.fill((0, 0, 0))
                            global v
                            v = 0
                        elif x is buttons[1]:
                            controls()
                            screen.fill((0, 0, 0))
                        elif x is buttons[2]:
                            about()
                            screen.fill((0, 0, 0))

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    exit()


def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()



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


def create_ascii_prediction(pred):
    return pred + 65
#    return(chr(pred+ 65))
    

def hand_choice_screen():
    screen.fill((0, 0, 0))
    running = True
    
    colors = [(105, 149, 0), (141, 91, 112), (0, 59, 86)]
    left_hand_button = pygame.Rect(20, 100, 300,300)    
    right_hand_button = pygame.Rect(470, 100, 300, 300)
    buttons = [left_hand_button, right_hand_button]
    button_words = ["Left Handed", "Right Handed"]
    
    global left_hand_global
    global right_hand_global
    
    for i, x in enumerate(buttons):
            text = pygame.font.Font("freesansbold.ttf", 30)
            text_s, text_r = text_objects(button_words[i], text)
            text_r.center = (x.centerx, x.centery)
            screen.blit(text_s, text_r)
    
    while running:

        pygame.draw.rect(screen, colors[0], left_hand_button, 10)
        pygame.draw.rect(screen, colors[1], right_hand_button, 10)
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in buttons:
                    if x.collidepoint(event.pos):
                        if x is buttons[0]:
                            left_hand_global = True
                            running = False
                        if x is buttons[1]:
                            right_hand_global = True
                            running = False
                            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if left_hand_global is False or right_hand_global is False:
                        print("Must pick which hand you want to use")
                    else:
                        running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                    
        pygame.display.update()

def game_screen():
    screen.fill((0, 0, 0))

    cover = pygame.Rect((math.floor(x_size * 0.65), math.floor(y_size * 0.05),
                         (math.floor(x_size * 0.75) - math.floor(x_size * 0.65)),
                         (math.floor(y_size * 0.15) - math.floor(y_size * 0.05))))
    cover2 = pygame.Rect((math.floor(x_size * 0.65), math.floor(y_size * 0.85),
                         (math.floor(x_size * 0.75) - math.floor(x_size * 0.65)),
                         (math.floor(y_size) - math.floor(y_size * 0.85))))

    running = True
    counter = 3
    current_val = None

    while running:
        # Video Processing
#        ret, frame = video_processor.start_video(cap)
#        if ret is None and frame is None:
#            running = False

        clock.tick(60)
        increment()
        # update counter to go from 3 to 0 and then capture the last inputted key event
        if v % 60 == 0:
            pygame.draw.rect(screen, (0, 0, 0), cover)
            counter -= 1
            if counter < 0:
                counter = 3
                # Video Processing
#                video_processor.write_image(frame)
#                video_processor.process_img()
#                #Prediction 
#                confidence, prediction = prediction_driver.get_prediction()
#                #DEBUG
#                print((confidence,prediction))
#                current_val = create_ascii_prediction(prediction)
                
            # Write the title text for this portion of the game
            text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
            text_s, text_r = text_objects(str(counter), text)
            text_r.center = (math.floor(x_size * 0.7), math.floor(y_size * 0.1))
            screen.blit(text_s, text_r)

        else:
            # Write the title text for this portion of the game
            text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
            text_s, text_r = text_objects(str(counter), text)
            text_r.center = (math.floor(x_size * 0.7), math.floor(y_size * 0.1))
            screen.blit(text_s, text_r)

        if counter == 3 and v % 60 == 0:
#            print(current_val)
            pygame.draw.rect(screen, (0, 0, 0), cover2)
            if current_val is None:
                # Write the title text for this portion of the game
                text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
                text_s, text_r = text_objects("NO INPUT", text)
                text_r.center = (math.floor(x_size * 0.7), math.floor(y_size * 0.9))
                screen.blit(text_s, text_r)
            else:
                # Write the title text for this portion of the game
                text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
                text_s, text_r = text_objects(chr(current_val), text)
                text_r.center = (math.floor(x_size * 0.7), math.floor(y_size * 0.9))
                screen.blit(text_s, text_r)
                current_val = None

        text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
        text_s, text_r = text_objects("Your character is: ", text)
        text_r.center = (math.floor(x_size * 0.4), math.floor(y_size * 0.9))
        screen.blit(text_s, text_r)

        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            button1 = pygame.Rect((math.floor(x_size * 0.2), math.floor(y_size * 0.2),
                                   (math.floor(x_size * 0.8) - math.floor(x_size * 0.2)),
                                   (math.floor(y_size * 0.8) - math.floor(y_size * 0.2))))

            pygame.draw.rect(screen, (255, 0, 0), button1)

            # Write the title text for this portion of the game
            text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
            text_s, text_r = text_objects("Please input a character in: ", text)
            text_r.center = (math.floor(x_size * 0.45), math.floor(y_size * 0.1))
            screen.blit(text_s, text_r)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                value = event.key
                for x in alphabet:
                    if value == x:
                        value = value_dict[x]
                    current_val = value

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        
    #Video Processing
#    video_processor.end_video(cap)

    return


def controls():
    screen.fill((0, 0, 0))

    running = True
    while running:
        # insert if needed for the future

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            pygame.display.update()
    return


def about():
    screen.fill((0, 0, 0))

    running = True
    while running:
        # insert if needed for the future

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            pygame.display.update()
    return


if __name__ == "__main__":
    # call the main function
    main()
