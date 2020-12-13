#!/usr/bin/env python3

import sys

class Ship:
    EAST = (0,1)
    WEST = (0,-1)
    NORTH = (1,0)
    SOUTH = (-1,0)

    RIGHT = -1
    LEFT = 1

    ccw_order = [EAST, NORTH, WEST, SOUTH]

    def __init__(self, direction, starting_pos = (0,0)):
        self.direction = direction
        self.position = starting_pos
    
    @staticmethod
    def _add_vec(pos, dpos):
        x,y = pos
        dx,dy = dpos

        return (x+dx,y+dy)

    def move_towards(self,direction, steps):
        x,y = direction
        direction = (x*steps, y*steps)
        self.position = Ship._add_vec(self.position, direction)

    def move_forward(self, steps):
        self.move_towards(self.direction,steps)
    
    def change_direction(self, d, steps):
        index = Ship.ccw_order.index(self.direction) + d*steps
        index = index % len(Ship.ccw_order)
        self.direction = Ship.ccw_order[index]

    def follow_command(self, command):
        c, steps = command[0], int(command[1:])
        turns = {'L' : Ship.LEFT,'R' : Ship.RIGHT}
        dirs = {'E' : Ship.EAST,'S': Ship.SOUTH,'N': Ship.NORTH,'W': Ship.WEST}
        moves = ['F']

        if c in turns:
            self.change_direction(turns[c], steps//90)
        elif c in dirs:
            self.move_towards(dirs[c], steps)
        elif c in moves:
            self.move_forward(steps)
            

    def follow_commands(self, commands):
        for comm in commands:
            self.follow_command(comm)
            print(self.position)

if __name__ == "__main__":
    FILENAME = "input.txt"
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    
    with open(FILENAME) as inp:
        commands = [line.strip() for line in inp.readlines()]
    
    ship = Ship(Ship.EAST)
    ship.follow_commands(commands)
    x,y = ship.position
    print(f'The position of the ship is {ship.position} and manhatten distance {abs(x) + abs(y)}')