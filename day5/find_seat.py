import sys

def find_seat_id(desc):
    seat = desc.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    return int(seat, base=2)

MAX = 1
FIND_SEAT = 2

if __name__ == "__main__":
    FILENAME = 'input.txt'
    OPTION = FIND_SEAT
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    if len(sys.argv) > 2:
        OPTION = sys.argv[2]
    
    with open(FILENAME) as f:
        if OPTION == MAX:
            m = max(find_seat_id(line.strip()) for line in f.readlines())
            print(f'Max: {m}')
        else:
            result = sorted(find_seat_id(line.strip()) for line in f.readlines())
            zipped = zip(result[:-1],result[1:])
            missing_seats = [x+1 for x,y in zipped if x + 1!=y]
            print(f'You can grab a seat at {missing_seats}')