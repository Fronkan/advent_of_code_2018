from math import floor
import numpy as np
from scipy import signal

serial_number = 8868  #From AoC website
#serial_number = 18 # For testing solution
power_matrix = [[floor(((((x+10)*y + serial_number)*(x+10))%1000)/100)-5 for x in range(1,301)] for y in range(1,301)]

# ------------------------------- Puzzle 1 -------------------------------
kernel = np.ones((3,3),dtype=int)
matrix = np.array(power_matrix)
corr_matrix = signal.correlate2d(matrix, kernel, mode="valid")
power = np.max(corr_matrix)
index = np.argmax(corr_matrix)
y,x = np.unravel_index(index, corr_matrix.shape)
print(f'Puzzle 1: ({x+1}, {y+1}), max power = {power}')


# ------------------------------- Puzzle 2 -------------------------------
max_power = 0
for size in range(1,300):
    kernel = np.ones((size,size),dtype=int)
    matrix = np.array(power_matrix)
    corr_matrix = signal.correlate2d(matrix, kernel, mode="valid")
    power = np.max(corr_matrix)
    index = np.argmax(corr_matrix)
    y,x = np.unravel_index(index, corr_matrix.shape)
    if power >= max_power:
        max_power = power
        best_x = x +1
        best_y = y +1
        best_size = size
    if size%10 == 0:
        print(round(size/300, 2))
print(f'Puzzle 2: pos=({best_x}, {best_y}); size={best_size}; power={max_power}')