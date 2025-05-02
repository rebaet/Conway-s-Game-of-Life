import gamelogic
import pygame
#import pygame_widgets
from sys import exit

# Colors
green = (80,130,100)
red = (130,80,100)

pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

# Game Parameters
fps = 10
alive_color = (200,200,200)
cell_size = 12
x_dim = 70
y_dim = 70

# Primary Surfaces
game_surface = pygame.Surface((850,850))
game_surface.fill((20,20,20))

stats_surface = pygame.Surface((275, 130))
stats_surface.fill((20,20,20))

# Button Surfaces
play_pause = pygame.Surface((275, 100))
clear = pygame.Surface((130, 100))
clear.fill((100,100,100))
rand = pygame.Surface((130, 100))
rand.fill((100,100,100))

text_font = pygame.font.Font("Minecraft.ttf", 25)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def draw_state(state, size):

    width = len(state[0])*size
    height = len(state)*size

    x = (850 - width) // 2
    y = (850 - height) // 2

    live_surface = pygame.Surface((width, height))

    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j]:
                pygame.draw.rect(live_surface, alive_color, (j*size, i*size, size, size), width=4)
            else:
                pygame.draw.rect(live_surface, (50,50,50), (j*size, i*size, size, size), width=4)

    game_surface.blit(live_surface, (x,y))

# Defaults
state = gamelogic.dummy_state(x_dim, y_dim)
generation = 0
paused = True
play_pause.fill(green)

# Game Loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Spacebar Play-Pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

        # Button Actions
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Play-Pause Button
            if 900 <= mouse_x < 1175 and 165 <= mouse_y < 265:
                paused = not paused

            # CLR Button(Cannot Unpause)
            if 900 <= mouse_x < 1030 and 280 <= mouse_y < 385:
                paused = True
                state = gamelogic.dummy_state(x_dim, y_dim)
                clear.fill((150,150,150))
                generation = 0

            # RAND Button(Cannot Unpause)
            if 1045 <= mouse_x < 1175 and 280 <= mouse_y < 385:
                paused = True
                state = gamelogic.random_state(x_dim, y_dim)
                rand.fill((150,150,150))
                generation = 0

        # Allowed actions when paused
        if paused:
            if event.type == pygame.MOUSEBUTTONDOWN:

                width = len(state[0]) * cell_size
                height = len(state) * cell_size
                x = (850 - width) // 2
                y = (850 - height) // 2

                # Change State of Cell
                if x <= mouse_x < x + width + cell_size*2 and y <= mouse_y < y + height + cell_size*2:
                    col = (mouse_x - x) // cell_size - 2
                    row = (mouse_y - y) // cell_size - 2
                    state[row][col] = 1 - state[row][col]
                    generation = 0

        # Refresh Button Color @ MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            clear.fill((100,100,100))
            rand.fill((100,100,100))

    # Change PLAY-PAUSE button color at BUTTONDOWN
    if event.type == pygame.MOUSEBUTTONDOWN and 900 <= mouse_x < 1175 and 165 <= mouse_y < 265:
        play_pause.fill((80,100,90))

    alive = gamelogic.count_alive(state)

    # Only Unpause if the game is paused, there are alive cells and the state is not stagnant
    if not paused and alive and state != gamelogic.next_state(state):
        state = gamelogic.next_state(state)
        generation += 1
    else:
        paused = True

    # Blit Game Surface
    draw_state(state, cell_size)
    screen.blit(game_surface, (25,25))

    # Blit Stats Surface
    screen.blit(stats_surface, (900,25))
    draw_text("Generation:    " + str(generation), text_font, green, 915, 55)
    draw_text("Live Cells:      " + str(alive), text_font, green, 915, 105)

    # Blit Buttons
    screen.blit(play_pause, (900, 165))
    if paused:
        play_pause.fill(green)
        draw_text("PLAY", text_font, (0,0,0), 1000, 205)
    else:
        play_pause.fill(red)
        draw_text("PAUSE", text_font, (0,0,0), 995, 205)
    
    screen.blit(clear, (900,280))
    draw_text("CLR", text_font, (0,0,0), 937, 320)
    
    screen.blit(rand, (1045,280))
    draw_text("RAND", text_font, (0,0,0), 1077, 320) 

    pygame.display.update()
    clock.tick(fps)