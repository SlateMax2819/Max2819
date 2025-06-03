import pygame
import time
import random
from PIL import Image

#initialize pygame
pygame.init()
pygame.mixer.init

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)
gold = (255, 215, 0)
silver = (192, 192, 192)
purple = (128, 0, 128)
bronze = (205, 127, 50)

#display
width = 600
height = 400
display_width = 1370
display_height = 775
SNAKE_SIZE = 50
SPEED = 10
FOOD_SIZE = SNAKE_SIZE 

#initialize display
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Sonic Game')
background_main = pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\SonicBackground.PNG")
background_main = pygame.transform.scale(background_main, (display_width, display_height))
background_death = pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\DeathScreen.PNG")
background_death = pygame.transform.scale(background_death, (display_width, display_height))
background_menu = pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\openmenu.PNG")
background_menu = pygame.transform.scale(background_menu, (display_width, display_height))

#Initialize the running images
# Load all frames into a list
sonic_frames = [
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 1.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 2.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 3.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 4.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 5.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 6.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 7.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 8.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 9.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame 10.PNG")
]
sonic_frames = [pygame.transform.scale(frame, (SNAKE_SIZE, SNAKE_SIZE)) for frame in sonic_frames]
# Load all frames into a list for Tails
tails_frames = [
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_1.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_2.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_3.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_4.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_5.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_6.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_7.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_8.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_9.PNG"),
    pygame.image.load("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\images\\running\\edited\\frame_10.PNG")
]
tails_frames = [pygame.transform.scale(frame, (SNAKE_SIZE, SNAKE_SIZE)) for frame in tails_frames]
#clock to control game speed
clock = pygame.time.Clock()

#sounds
menu_music = pygame.mixer.Sound("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\music\\opentheme.wav")
game_music = pygame.mixer.Sound("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\music\\Sonic_theme.wav")
eat_sound = pygame.mixer.Sound("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\music\\ring_effect.wav")
death_sound = pygame.mixer.Sound("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\music\\oh_no_1.wav")
death_screen = pygame.mixer.Sound("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\music\\gameover.wav")
game_announcment = pygame.mixer.Sound("F:\\Windows Folders\\Documents\\code docs\\games\\snonic game\\resources\\music\\eggnouncement.wav")

#font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])

#main game loop
def gameloop():
    game_open = True
    game_over = False
    game_close = False

    x = (width // SNAKE_SIZE // 2) * SNAKE_SIZE
    y = (height // SNAKE_SIZE // 2) * SNAKE_SIZE
    x_change = 0
    y_change = 0

    # Initialize the snake
    snake = []
    length = 1
    food_x = round(random.randrange(0, width - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
    food_y = round(random.randrange(0, height - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
    menu_music.play(-1)  # Loop the menu music

    # Animation variables for the snake
    frame_index = 0
    frame_delay = 5  # Adjust for speed of animation
    frame_counter = 0
    frame_tails_index = 0
    frame_tails_delay = 5  # Adjust for speed of animation
    frame_tails_counter = 0
    
    while game_open:
        screen.blit(background_menu, (0, 0))
        # Display the menu
        message("WELCOME TO A SONIC ADVENTURE!", black, width / 1.3, height / 11)
        message("BITCH ASS QUITER!  Q=QUIT", bronze, width / .65, height / 7)
        message("PLAY!   P=PLAY", gold, width / 2.1, height / 7)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True
                    game_open = False
                if event.key == pygame.K_p:
                    menu_music.stop()
                    game_music.play(-5)
                    game_music.set_volume(.4)
                    game_open = False
                    game_close = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
    while not game_over:
        while game_close:
            game_music.stop()
            screen.blit(background_death, (0, 0))
                # Play game over music once
            if not pygame.mixer.get_busy():
                game_announcment.play()  # Play the game announcement sound
                death_screen.play()
                death_sound.set_volume(0.5)  # Set volume for death sound
            message("YOU FUCKIN DIED!!", red, width / 1, height / 11)
            message("BITCH ASS QUITER!  Q=QUIT", bronze, width / .58, height / 6)
            message("RESTART C=REPLAY", gold, width / 6.5, height / 6)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        death_screen.stop()  # Stop the music if quitting like bitch
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        death_screen.stop()  # Stop the music if restarting
                        gameloop()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                        return
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                if event.key == pygame.K_a:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_d:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_w:
                    y_change = -SNAKE_SIZE
                    x_change = 0
                elif event.key == pygame.K_s:
                    y_change = SNAKE_SIZE
                    x_change = 0
                    
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            game_close = True
            
# Update snake position

        x += x_change
        y += y_change
        screen.blit(background_main, (0, 0))
        
        # Use the 'tails' image for food
        screen.blit(tails_frames[frame_tails_index], (food_x, food_y))

        # Update frame index only when moving
        if x_change != 0 or y_change != 0:
            frame_tails_counter += 1
            if frame_tails_counter >= frame_tails_delay:
                frame_tails_index = (frame_tails_index + 1) % len(tails_frames)
                frame_tails_counter = 0
                
        snake.append([x, y])
        if len(snake) > length:
            del snake[0]
            
        for segment in snake:
            screen.blit(sonic_frames[frame_index], (segment[0], segment[1]))

        # Update frame index only when moving
        if x_change != 0 or y_change != 0:
            frame_counter += 1
            if frame_counter >= frame_delay:
                frame_index = (frame_index + 1) % len(sonic_frames)
                frame_counter = 0

        # Check if the snake has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
            food_y = round(random.randrange(0, height - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
            eat_sound.play()  # Play sound when eating food
            length += 1

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()
    quit()

gameloop()
# This is the main entry point for the game
pygame.quit()
quit()
