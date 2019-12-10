# game_of_life
An implementation of Conway's Game of Life in pygame

Deps: pygame

The program takes command line arguments. Usage:

python life_engine.pyw [x] [y]
python life_engine.pyw [x] [y] [size of cells]
python life_engine.pyw [x] [y] [size of cells] [fps]

Defaults are: x = 25
              y = 25
              size of cells = 15
              fps = 15
              
Controls:
  Toggle cells on and off with the mouse.
  Step through generations with N.
  Clear board with C.
  Let simulation run with Space.
  Quit with Q.
