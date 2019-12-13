from enum import Enum
import pygame

class State(Enum):
    DEAD = 1
    ALIVE = 2


class Cell:
    def __init__(self, x, y, state=State.DEAD, scale=10):
        self.x = x
        self.y = y
        self.state = state
        self.scale = scale
        self.rect = pygame.Rect(self.x * self.scale, self.y * self.scale, self.scale, self.scale)
        self.live_neighbours = 0

        
    def __repr__(self):
        return f'Cell [{self.x}],[{self.y}]'

        
    def count_live_neighbours(self, cells_list, max_x, max_y):
        self.live_neighbours = 0

        # this is the complicated but fast way
        if self.x == 0 and self.y == 0:                      # top left corner
            if cells_list[self.x][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x == 0 and self.y == max_y - 1:            # bottom left corner
            if cells_list[self.x][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x == max_x - 1 and self.y == max_y - 1:    # bottom right corner
            if cells_list[self.x - 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x == max_x - 1 and self.y == 0:            # top right corner
            if cells_list[self.x - 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x < max_x - 1 and self.y == max_y - 1:    # bottom edge
            if cells_list[self.x - 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x == 0 and self.y > 0:                    # left edge
            if cells_list[self.x][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x == max_x - 1 and self.y < max_y - 1:    # right edge
            if cells_list[self.x][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1

        elif self.x > 0 and self.y == 0:                    # top edge
            if cells_list[self.x - 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
                
        else:                                                # middle cells
            if cells_list[self.x][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x + 1][self.y - 1].state == State.ALIVE:
                self.live_neighbours+= 1
            if cells_list[self.x - 1][self.y + 1].state == State.ALIVE:
                self.live_neighbours+= 1
        

        # this is the simple but really slow way
        
        # for line in cells_list:
        #     for cell in line:
        #         if cell.x == self.x - 1:
        #             if cell.y == self.y - 1:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #             if cell.y == self.y:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #             if cell.y == self.y + 1:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #         if cell.x == self.x:
        #             if cell.y == self.y - 1:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #             if cell.y == self.y + 1:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #         if cell.x == self.x + 1:
        #             if cell.y == self.y - 1:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #             if cell.y == self.y:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1
        #             if cell.y == self.y + 1:
        #                 if cell.state == State.ALIVE:
        #                     self.live_neighbours+= 1

        
    def am_i_alive(self, rule="life"):
        if rule == "life":
            if self.state == State.ALIVE:
                if self.live_neighbours != 2 and self.live_neighbours != 3:
                    self.toggle()
            elif self.state == State.DEAD:
                if self.live_neighbours == 3:
                    self.toggle()
                    
        elif rule == "highlife":
            if self.state == State.ALIVE:
                if self.live_neighbours != 2 and self.live_neighbours != 3:
                    self.toggle()
            elif self.state == State.DEAD:
                if self.live_neighbours == 3 or self.live_neighbours == 6:
                    self.toggle()

        elif rule == "morley":
            if self.state == State.ALIVE:
                if (self.live_neighbours != 2 and self.live_neighbours != 4 and
                    self.live_neighbours != 5):
                    self.toggle()
            elif self.state == State.DEAD:
                if (self.live_neighbours == 3 or self.live_neighbours == 6 or
                    self.live_neighbours == 8):
                    self.toggle()

        elif rule == "2x2":
            if self.state == State.ALIVE:
                if (self.live_neighbours != 1 and self.live_neighbours != 2 and
                    self.live_neighbours != 5):
                    self.toggle()
            elif self.state == State.DEAD:
                if self.live_neighbours == 3 or self.live_neighbours == 6:
                    self.toggle()

        elif rule == "daynight":
            if self.state == State.ALIVE:
                if (self.live_neighbours != 3 and self.live_neighbours != 4 and
                    self.live_neighbours != 6 and self.live_neighbours != 7 and
                    self.live_neighbours != 8):
                    self.toggle()
            elif self.state == State.DEAD:
                if (self.live_neighbours == 3 or self.live_neighbours == 6 or
                    self.live_neighbours == 7 or self.live_neighbours == 8):
                    self.toggle()
                    
        elif rule == "inkspot":
            if self.state == State.DEAD:
                if self.live_neighbours == 3:
                    self.toggle()
            elif self.state == State.ALIVE:
                pass
                    
        elif rule == "replicator":
            if self.state == State.ALIVE:
                if (self.live_neighbours != 1 and self.live_neighbours != 3 and
                    self.live_neighbours != 5 and self.live_neighbours != 7):
                    self.toggle()
            elif self.state == State.DEAD:
                if (self.live_neighbours == 1 or self.live_neighbours == 3 or
                    self.live_neighbours == 5 or self.live_neighbours == 7):
                    self.toggle()

                    
    def toggle(self):
        if self.state == State.ALIVE:
            self.state = State.DEAD
        else:
            self.state = State.ALIVE

        return self.state
