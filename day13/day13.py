from enum import Enum
from copy import deepcopy


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

def num2Direction(num):
    val = num % 4
    if val == 0:
        return Direction.RIGHT
    elif val == 1:
        return Direction.DOWN
    elif val == 2:
        return Direction.LEFT
    elif val == 3:
        return Direction.UP
    else:
        print("PANIC: Bad direction")


def ascii2direction(symbol):
    if symbol == ">":
        return Direction.RIGHT
    elif symbol == "<":
        return Direction.LEFT
    elif symbol == "^":
        return Direction.UP
    elif symbol == "v":
        return Direction.DOWN
    else:
        print("Bad Direction")
        print("Exiting...")
        exit() 

def is_intersection(rail):
    return rail == "+"

def is_turn(rail):
    return rail == "/" or rail == "\\"

class Cart:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.intersect_cnt = 0 
        self.direction = direction
        self.is_crashed = False
        self.prev = self.position()

    def __repr__(self):
        return f'(pos: {self.position()}, direction: {self.direction}, crashed: {self.is_crashed})'

    def position(self):
        return (self.col, self.row)

    def crashed(self):
        self.is_crashed = True

    def tick(self, rail):
        if rail == " ":
            print("PANIC: Not on rail")
            print(f'{self.position}')
            exit()
        self.set_direction(rail)
        self.move()

    def move(self):
        self.prev = self.position()
        if self.direction == Direction.LEFT:
            self.col -= 1
        elif self.direction == Direction.RIGHT:
            self.col += 1
        elif self.direction == Direction.UP:
            self.row -= 1
        elif self.direction == Direction.DOWN:
            self.row += 1

    def set_direction(self, rail):
        if is_intersection(rail):
            self.intersection()
        elif is_turn(rail):
            self.turn(rail)

    def turn(self, rail):
        if rail == "/" and self.direction == Direction.UP :
            self.direction = Direction.RIGHT
        elif rail == "/" and self.direction == Direction.LEFT:
            self.direction = Direction.DOWN
        elif rail == "/" and self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        elif rail == "/" and self.direction == Direction.RIGHT:
            self.direction = Direction.UP

        elif rail == "\\" and self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        elif rail == "\\" and self.direction == Direction.LEFT:
            self.direction = Direction.UP
        elif rail == "\\" and self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif rail == "\\" and self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
        else:
            print("PANIC: Bad combination of direction and rail")
            print(f'Directions: {self.direction}, rail: {rail}, position: {self.position()}')
            print("Exiting...")
            exit()

    def intersection(self):
        #print(f'{self.direction}, {self.intersection_direction_change()}, {num2Direction(self.direction.value + self.intersection_direction_change())}')
        self.direction = num2Direction(self.direction.value + self.intersection_direction_change())
        self.intersect_cnt = (self.intersect_cnt +1)%3

    def intersection_direction_change(self):
        return self.intersect_cnt - 1


def puzzle1(tracks, carts):
    crash = False
    crash_pos = None
    while not crash:
        cart_pos = []
        for cart in carts:
            cart.tick(tracks[cart.row][cart.col])
            pos = cart.position()
            if pos in cart_pos:
                crash_pos = pos
                crash = True
                break
            else:
                cart_pos.append(cart.position())
        
        for cart in carts:
            for other in carts:
                # Crashing with trains when switching place
                if (cart.prev == other.position()) and (cart.position() == other.prev):
                    crash_pos = pos
                    crash = True
                    break
            if crash:
                break
    return crash_pos

def puzzle2(tracks, carts):
    while len(carts) > 1:
        cart_positions = {}
        for cart in carts:
            cart.tick(tracks[cart.row][cart.col])
            pos = cart.position()
            if not pos in cart_positions:
                cart_positions[pos] = cart
            else:
                # We have a crash
                cart_positions[pos].crashed()
                cart.crashed()

        for cart in carts:
            for other in carts:
                # Crashing with trains when switching place
                if (cart.prev == other.position()) and (cart.position() == other.prev):
                    cart.crashed()
                    other.crashed()

        carts = list(filter(lambda cart: not cart.is_crashed , carts))
    return carts[0].position()


tracks = []
carts = []
with open("day13_data.txt") as f:
    row_cnt = 0
    for row in f:
        row_list = []
        col_cnt = 0
        for val in row:
            if val == ">" or val == "<":
                row_list.append("-")
                carts.append(Cart(row_cnt, col_cnt, ascii2direction(val)))
            elif val == "v" or val == "^":
                row_list.append("|")
                carts.append(Cart(row_cnt, col_cnt, ascii2direction(val)))
            elif val == "\n":
                continue
            else:
                row_list.append(val)
            col_cnt += 1
        tracks.append(row_list)
        row_cnt += 1

print(f'Puzzle 1: {puzzle1(tracks, deepcopy(carts))}')
print(f'Puzzle 2: {puzzle2(tracks,deepcopy(carts))}')

