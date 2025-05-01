import gamelogic
import pygame
from sys import exit

# Colors
green = (80,130,100)
red = (130,80,100)

pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

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

# Game Parameters
fps = 10
alive_color = (200,200,200)
cell_size = 12
x_dim = 70
y_dim = 70

text_font = pygame.font.SysFont("Courier", 25)
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

def handle_mouse_click(state, size):
    width = len(state[0]) * size
    height = len(state) * size

    x = (850 - width) // 2
    y = (850 - height) // 2
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if x <= mouse_x < x + width and y <= mouse_y < y + height:
        col = (mouse_x - x) // size - 2
        row = (mouse_y - y) // size - 2

        state[row][col] = 1 - state[row][col]

# Defaults
state = gamelogic.random_state(x_dim, y_dim)
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

        if paused:
            if event.type == pygame.MOUSEBUTTONDOWN:

                handle_mouse_click(state, cell_size)

                width = len(state[0]) * cell_size
                height = len(state) * cell_size
                x = (850 - width) // 2
                y = (850 - height) // 2

                # Change State of Cell
                if x <= mouse_x < x + width and y <= mouse_y < y + height:
                    generation = 0
                 # CLR Button
                if 900 <= mouse_x < 1030 and 280 <= mouse_y < 385:
                    state = gamelogic.dummy_state(x_dim, y_dim)
                    generation = 0
                # RND Button
                if 1045 <= mouse_x < 1175 and 280 <= mouse_y < 385:
                    state = gamelogic.random_state(x_dim, y_dim)
                    generation = 0
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Play-Pause Button
            if 900 <= mouse_x < 1175 and 165 <= mouse_y < 265:
                paused = not paused

    # Move to Next Gen
    if not paused:  
        state = gamelogic.next_state(state)    
        generation += 1 

    draw_state(state, cell_size)
    screen.blit(game_surface, (25,25))

    alive = gamelogic.count_alive(state)
    screen.blit(stats_surface, (900,25))
    draw_text("Generation: " + str(generation), text_font, green, 915, 50)
    draw_text("Live Cells: " + str(alive), text_font, green, 915, 100)

    # Blit Buttons
    screen.blit(play_pause, (900, 165))
    if paused:
        play_pause.fill(green)
        draw_text("PLAY", text_font, (0,0,0), 1000, 200)
    else:
        play_pause.fill(red)
        draw_text("PAUSE", text_font, (0,0,0), 995, 200)

    screen.blit(clear, (900,280))
    draw_text("CLR", text_font, (0,0,0), 940, 316)
    
    screen.blit(rand, (1045,280))
    draw_text("RND", text_font, (0,0,0), 1090, 316) 

    pygame.display.update()
    clock.tick(fps)