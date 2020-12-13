#!/usr/bin/env python3

import sys
import copy

EMPTY = 'L'
FLOOR = '.'
OCCUP = '#'



def get_adjacent(seats, row, col):
    max_rows = len(seats) - 1
    max_cols = len(seats[0]) - 1
    def walk_direction(pos, dpos):
        y,x = pos
        dy,dx = dpos
        return (y+dy,x+dx)
    def on_grid(pos):
        y,x = pos
        return (0 <= y <= max_rows) and (0 <= x <= max_cols)
    
    def find_seat(pos,direction):
        pos = walk_direction(pos,direction)
        while on_grid(pos):
            y,x = pos
            if seats[y][x] != FLOOR:
                break
            pos = walk_direction(pos,direction)
        return pos
    
    adj = []
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            direction = (dy,dx)
            if direction == (0,0):
                continue
            a = find_seat((row,col), (dy,dx))
            adj.append(a)


    return [pos for pos in adj if on_grid(pos)]
    

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    

    with open(FILENAME) as inp:
        seats = [list(line.strip()) for line in inp.readlines() if line.strip()]
    old_seats = None
    new_seats = seats
    while old_seats != new_seats:
        old_seats = copy.deepcopy(new_seats)
        for row_idx, row in enumerate(old_seats):
            for col_idx, seat in enumerate(row):
                adjacent = get_adjacent(old_seats, row_idx, col_idx)
                
                if seat == EMPTY and all([old_seats[r][c] != OCCUP for r,c in adjacent]):
                    new_seats[row_idx][col_idx] = OCCUP
                elif seat == OCCUP and len([1 for r,c in adjacent if old_seats[r][c] == OCCUP]) >= 5:
                    new_seats[row_idx][col_idx] = EMPTY
                else:
                    new_seats[row_idx][col_idx] = seat
    
    occupied = 0
    for row in old_seats:
        for seat in row:
            occupied += 1 if seat == OCCUP else 0
    print(occupied)
