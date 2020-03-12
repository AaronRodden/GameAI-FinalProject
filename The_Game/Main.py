import pygame
import math
import random

import os
import cv2
from lib import video_processor
from classifiers import prediction_driver

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

cap = cv2.VideoCapture(0)
pygame.init()

# X MUST BE LARGER THAN Y
# use these to scale the buttons with the screen
x_size = 1200
y_size = 800
#Define the clock and the global counter
clock = pygame.time.Clock()
v = 0

screen = pygame.display.set_mode((x_size, y_size))

pygame.display.set_caption("Sign Language Recognition Game")

#Used for determining characters
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

###IMAGE IMPLEMENTATION (Comment these out to remove this part of the game)
images = {'a': pygame.image.load('Images/A.jpg'),'o': pygame.image.load('Images/O.jpg'),
            'y': pygame.image.load('Images/Y.jpg'), 'v': pygame.image.load('Images/V.jpg'),
            'w': pygame.image.load('Images/W.jpg')}

image_keys = ['a','o','y','v','w']
###END SECTION

#Don't change
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
        clock.tick(60)
        buttons = button_make()
        color_count = len(colors) - 1

        #draw buttons
        for x in buttons:
            pygame.draw.rect(screen, colors[color_count], x, scale)
            color_count -= 1

        word_count = len(button_words) - 1

        #Display the button text
        for x in buttons:
            text = pygame.font.Font("freesansbold.ttf", math.floor(x.height / 2))
            text_s, text_r = text_objects(button_words[word_count], text)
            text_r.center = (x.centerx, x.centery)
            screen.blit(text_s, text_r)
            word_count -= 1

        #If button pressed switch states
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in buttons:
                    if x.collidepoint(event.pos):
                        if x is buttons[0]:
                            game_screen()
                            screen.fill((0, 0, 0))
                            global v
                            v = 0
                            ###IMAGE IMPLEMENTATION (Comment these out to remove this part of the game)
                            global image_keys
                            image_keys = ['a','o','y','v','w']
                            ###END
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

#Make text
def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()


# make the buttons for the main screen
def button_make():
    # draw on screen, color, place, and make just outline fill

    #Start button
    button1 = pygame.Rect((math.floor(x_size * 0.3), math.floor(y_size * 0.25),
                           (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                           (math.floor(y_size * 0.35) - math.floor(y_size * 0.25))))

    #Controls button
    button2 = pygame.Rect((math.floor(x_size * 0.3), math.floor(y_size * 0.55),
                           (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                           (math.floor(y_size * 0.65) - math.floor(y_size * 0.55))))

    #About button
    button3 = pygame.Rect((math.floor(x_size * 0.3), math.floor(y_size * 0.85),
                           (math.floor(x_size * 0.7) - math.floor(x_size * 0.3)),
                           (math.floor(y_size * 0.95) - math.floor(y_size * 0.85))))

    buttons = [button1, button2, button3]

    return buttons

def create_ascii_prediction(pred):
    return pred + 65
#    return(chr(pred+ 65))

#main game work
def game_screen():
    screen.fill((0, 0, 0))
    current_word = []

    #Cover the timer
    cover = pygame.Rect((math.floor(x_size * 0.65), math.floor(y_size * 0.05),
                         (math.floor(x_size * 0.75) - math.floor(x_size * 0.65)),
                         (math.floor(y_size * 0.15) - math.floor(y_size * 0.05))))

    #Cover the character
    cover2 = pygame.Rect((math.floor(x_size * 0.58), math.floor(y_size * 0.85),
                         (math.floor(x_size * 0.85) - math.floor(x_size * 0.55)),
                         (math.floor(y_size) - math.floor(y_size * 0.85))))

    ###SENTENCE FORMING IMPLEMENTATION
    #Cover the text of the word
    # cover3 = pygame.Rect((math.floor(x_size * 0.1), math.floor(y_size * 0.4),
    #                      (math.floor(x_size * 0.9) - math.floor(x_size * 0.1)),
    #                      (math.floor(y_size * 0.6) - math.floor(y_size * 0.4))))
    ###END

    ###IMAGE IMPLEMENTATION (Comment these out to remove this part of the game)
    cover4 = pygame.Rect((math.floor(x_size * 0.1), math.floor(y_size * 0.25),
                         (math.floor(x_size * 0.15) - math.floor(x_size * 0.1)),
                         (math.floor(y_size * 0.75) - math.floor(y_size * 0.25))))

    cover5 = pygame.Rect((math.floor(x_size * 0.85), math.floor(y_size * 0.25),
                         (math.floor(x_size * 0.9) - math.floor(x_size * 0.85)),
                         (math.floor(y_size * 0.75) - math.floor(y_size * 0.25))))
    ###END

    counter = 3
    current_val = None
    running = True

    ###IMAGE IMPLEMENTATION (Comment these out to remove this part of the game)
    image_count = 5
    curr_img = image_keys.pop(random.randrange(0, image_count))
    screen.blit(images[curr_img], (x_size * 0.3, y_size * 0.3))
    ###END

    while running:
        # Video Processing
        ret, frame = video_processor.start_video(cap)
        if ret is None and frame is None:
            running = False

        clock.tick(60)
        increment()

        # Write character input prompt
        text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
        text_s, text_r = text_objects("Please input a character in: ", text)
        text_r.center = (math.floor(x_size * 0.45), math.floor(y_size * 0.1))
        screen.blit(text_s, text_r)

        #Write last character prompt
        text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
        text_s, text_r = text_objects("Your last character is: ", text)
        text_r.center = (math.floor(x_size * 0.4), math.floor(y_size * 0.9))
        screen.blit(text_s, text_r)

        #check events for data storage or exiting
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

                ###SENTENCE FORMING IMPLEMENTATION
                # if event.key == pygame.K_RETURN:
                #     current_word.clear()
                #     pygame.draw.rect(screen, (0, 0, 0), cover3)
                #     break
                ###END

                #store key and then assign it to respective alphabet character
                value = event.key
                for x in alphabet:
                    if value == x:
                        value = value_dict[x]
                    current_val = value

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # update counter to go from 3 to 0 and then capture the last inputted key event
        ###BIGNOTE
        ###IF YOU NEED TO SLOW DOWN OR SPEED UP COUNTER CHANGE THE VALUE AFTER % < is faster > is slower

        #reduce 1 "second" and then refresh counter, if less than 0 reset counter
        #if still counting just continue
        if v % 4 == 0:
            pygame.draw.rect(screen, (0, 0, 0), cover)
            counter -= 1
            if counter < 0:
                counter = 3
                # Video Processing
                video_processor.write_image(frame)
                video_processor.process_img()
                #Prediction
                confidence, prediction = prediction_driver.get_prediction()
                #DEBUG
                print((confidence,prediction))
                current_val = create_ascii_prediction(prediction)
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

        ###BIGNOTE
        ###IF YOU NEED TO SLOW DOWN OR SPEED UP COUNTER CHANGE THE VALUE AFTER % < is faster > is slower

        #if the counter ends then cover the chacter and display new values accordingly
        if counter == 3 and v % 4 == 0:
            pygame.draw.rect(screen, (0, 0, 0), cover2)

            #if no value in last 3 seconds display no input
            if current_val is None:
                # Write the title text for this portion of the game
                text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.03))
                text_s, text_r = text_objects("NO INPUT", text)
                text_r.center = (math.floor(x_size * 0.7), math.floor(y_size * 0.9))
                screen.blit(text_s, text_r)

                #only used to denote incorrect for image implementation
                ###IMAGE IMPLEMENTATION
                pygame.draw.rect(screen, (255, 0, 0), cover4)
                pygame.draw.rect(screen, (255, 0, 0), cover5)
                ###END
            else:
                #if a current value is defined then do manipulations
                # Write current value
                text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.05))
                text_s, text_r = text_objects(chr(current_val), text)
                text_r.center = (math.floor(x_size * 0.7), math.floor(y_size * 0.9))
                screen.blit(text_s, text_r)

                ###IMAGE IMPLEMENTATION
                #see if the input and image character are equal
                if chr(current_val) == curr_img:
                    image_count -= 1
                    #if array is empty then reset it
                    if image_count == 0:
                            image_keys.append('a')
                            image_keys.append('o')
                            image_keys.append('y')
                            image_keys.append('v')
                            image_keys.append('w')
                            image_count = 5
                    #get the next image, draw correct markers and then display
                    curr_img = image_keys.pop(random.randrange(0, image_count))
                    pygame.draw.rect(screen, (0, 255, 0), cover4)
                    pygame.draw.rect(screen, (0, 255, 0), cover5)
                    screen.blit(images[curr_img], (x_size * 0.3, y_size * 0.3))
                #if incorrect markers are red
                else:
                    pygame.draw.rect(screen, (255, 0, 0), cover4)
                    pygame.draw.rect(screen, (255, 0, 0), cover5)
                ###END

                #serntences stored into a list and then written out until RETURN is pressed
                # or they reach the right side threshhold of making too large a word
                ###SENTENCE FORMING IMPLEMENTATION
                # current_word.append(current_val)
                #
                # if len(current_word) != 0:
                #     offset = 0
                #     for x in current_word:
                #         text = pygame.font.Font("freesansbold.ttf", math.floor(x_size * 0.05))
                #         text_s, text_r = text_objects(chr(x), text)
                #         text_r.center = (math.floor(x_size * (0.2 + offset)), math.floor(y_size * 0.5))
                #         screen.blit(text_s, text_r)
                #         offset += 0.05
                #         if offset > 0.70:
                #             current_word.clear()
                #             pygame.draw.rect(screen, (0, 0, 0), cover3)
                #             break
                ###END

                current_val = None

        pygame.display.update()

    #Video Processing
    video_processor.end_video(cap)

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
