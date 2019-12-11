#! usr/bin/env python3

from enum import Enum
from cell import Cell, State
import pygame
import sys

class GameState(Enum):
    SETUP = 1
    RUNNING = 2

    
def update_neighbours(list_of_cells, max_x, max_y):
    for line in list_of_cells:
        for cell in line:
            cell.count_live_neighbours(list_of_cells, max_x, max_y)

            
def update_living(list_of_cells, rule):
    for line in list_of_cells:
        for cell in line:
            cell.am_i_alive(rule)

            
def calc_next_round(list_of_cells, max_x, max_y, rule): 
    update_neighbours(list_of_cells, max_x, max_y)
    update_living(list_of_cells, rule)
            

def generate_list_of_cells(x, y, scale_factor):
    main_list = []

    j = 0
    
    while j < x:
        i = 0
        inner_list = []
        while i < y:
            inner_list.append(Cell(j, i, scale=scale_factor))
            i += 1
        main_list.append(inner_list)
        j += 1

    return main_list


def print_cells(list_of_cells, screen):
    for line in list_of_cells:
        for cell in line:
            if cell.state == State.ALIVE:
                pygame.draw.rect(screen, live_colour, cell.rect)
            else:
                pygame.draw.rect(screen, dead_colour, cell.rect)


def draw_grid(x, y, scale, screen):
    for i in range(1, x):
        pygame.draw.line(screen, grid_colour, (i * scale, 0), (i * scale, y * scale - 1))

    for i in range(1, y):
        pygame.draw.line(screen, grid_colour, (0, i * scale), (x * scale - 1, i * scale))

        
def clear_board(cell_list):
    for line in cell_list:
        for cell in line:
            cell.state = State.DEAD


def update_all(screen, x, y, scale, fps, cell_list,
               game_state, clock, calc_next, rule):
    if calc_next:
        calc_next_round(cell_list, x, y, rule)
        
    print_cells(cell_list, screen)
    draw_grid(x, y, scale, screen)
    
    if game_state == GameState.RUNNING:
        clock.tick(fps)
        
    pygame.display.update()

            
def engine(x, y, scale, fps, rule="life"):
    print(f"x = {x}\ny = {y}\ncell size = {scale}\nfps = {fps}\nrule = {rule}")
    
    size = width, height = x * scale, y * scale
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game of Life')
    screen.fill((64, 64, 64))
    clock = pygame.time.Clock()

    cell_list = generate_list_of_cells(x, y, scale)
    
    game_state = GameState.SETUP
    calc_next = False

    update_all(screen, x, y, scale, fps, cell_list,
               game_state, clock, calc_next, rule)
    
    while True:
        if game_state == GameState.SETUP:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = GameState.RUNNING
                    elif event.key == pygame.K_n:
                        calc_next = True
                        update_all(screen, x, y, scale, fps, cell_list,
                                   game_state, clock, calc_next, rule)
                        calc_next = False
                    elif event.key == pygame.K_c:
                        clear_board(cell_list)
                        update_all(screen, x, y, scale, fps, cell_list,
                                   game_state, clock, calc_next, rule)
                    elif event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for line in cell_list:
                        for cell in line:
                            if cell.rect.collidepoint(mouse_pos):
                                cell.toggle()
                    update_all(screen, x, y, scale, fps, cell_list,
                               game_state, clock, calc_next, rule)
    
        elif game_state == GameState.RUNNING:
            calc_next = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_n:
                        game_state = GameState.SETUP
                    
            update_all(screen, x, y, scale, fps, cell_list,
                       game_state, clock, calc_next, rule)
            calc_next = False

# global colour names
live_colour = (241, 222, 8)
dead_colour = (64,  64, 64)
grid_colour = (150, 150, 150)

if __name__ == '__main__':
    pygame.init()
    
    if len(sys.argv) == 3:
        engine(int(sys.argv[1]), int(sys.argv[2]), 15, 15)
    elif len(sys.argv) == 4:
        engine(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), 15)
    elif len(sys.argv) == 5:
        engine(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
               int(sys.argv[4]))
    elif len(sys.argv) == 6:
        engine(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
               int(sys.argv[4]), rule=str(sys.argv[5]))
    else:
        print("Starting with default options:")
        engine(25, 25, 15, 15)
