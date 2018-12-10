import re
from copy import deepcopy
from collections import namedtuple


Position = namedtuple('Position', ['x', 'y'])
Velocity = namedtuple('Velocity', ['x', 'y'])


class Light:
    def __init__(self, x,y,dx,dy):
        self.pos = Position(int(x),int(y))
        self.vel = Velocity(int(dx),int(dy))

    def __repr__(self):
        return f'[{self.pos}:{self.vel}]'

    def step(self):
        self.pos = Position(self.pos.x + self.vel.x, self.pos.y + self.vel.y)
        return self.pos

class Sky:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.reset_map()

    def reset_map(self):
        self.map = [["." for x in range(x_max + abs(x_min)+1)] for y in range(y_max + abs(y_min)+1)]

    def add_lights(self,lights):
        for light in lights:
            self.add_light(light)

    def add_light(self,light):
        self.map[abs(self.y_min) + light.pos.y][abs(self.x_min)+light.pos.x] = "#"

    def __repr__(self):
        output = ""
        for row in self.map:
            row_str = "".join(row)
            output = output + row_str +"\n"
        return output



# Script
lights = list(map(lambda num_list: Light(*num_list), [re.findall(r"[+-]?\d+(?:\.\d+)?", line) for line in open("day10_data.txt")]))


xs = list(map(lambda l: l.pos.x, lights))
ys = list(map(lambda l: l.pos.y, lights))
x_min = min(xs)
x_max = max(xs)
y_min = min(ys)
y_max = max(ys)
area = (x_max - x_min)*(y_max-y_min) 
min_area = area

cnt = 1
best_lights = []
while cnt < 20000:
    for light in lights:
        light.step()

    xs = list(map(lambda l: l.pos.x, lights))
    ys = list(map(lambda l: l.pos.y, lights))
    x_min = min(xs)
    x_max = max(xs) 
    y_min = min(ys)
    y_max = max(ys)    

    area = (x_max - x_min)*(y_max-y_min) 
    if area < min_area:
        min_area = area
        itter = cnt
        best_lights = deepcopy(lights)
    cnt +=1



xs = list(map(lambda l: l.pos.x, best_lights))
ys = list(map(lambda l: l.pos.y, best_lights))
x_min = min(xs)
x_max = max(xs) 
y_min = min(ys)
y_max = max(ys)    

sky = Sky(x_min,x_max, y_min, y_max)
sky.add_lights(best_lights)
print(f'Number of seconds (puzzel2): {itter}')
print("Message:")
print(sky)

"""
print(best_x_min)
print(best_x_max)
print(best_y_min)
print(best_y_max)
"""












