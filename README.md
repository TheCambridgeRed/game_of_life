# game_of_life
An implementation of Conway's Game of Life using pygame

Dependencies: pygame

Usage:

* python3 life_engine.pyw help
* python3 life_engine.pyw
* python3 life_engine.pyw [x] [y]
* python3 life_engine.pyw [x] [y] [size of cells]
* python3 life_engine.pyw [x] [y] [size of cells] [fps]
* python3 life_engine.pyw [x] [y] [size of cells] [fps] [rule]

Defaults: 
* x = 25
* y = 25
* size of cells = 15
* fps = 15
* rule = life

Options for rules (rule specification) - code:
* Life (B3/S23) - life
* HighLife (B36/S23) - highlife
* Morley (B368/S245) - morley
* 2x2 (B36/S125) - 2x2
* Day & Night (B3678/S34678) - daynight
* Life Without Death (B3/S012345678) - inkspot
* Replicator (B1357/S1357) - replicator
              
Controls:
* When simulation is stopped: Toggle cells on and off with the mouse (click and drag to paint and erase). Clear board with C.
* Step through generations with N (press and hold to run simulation)
* Let simulation run with Space.
* Quit with Q.
