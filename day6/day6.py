import string

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def puzzel1(coordinates):

    max_x = max([val[0] for val in coordinates]) +1
    max_y = max([val[1] for val in coordinates]) +1 
    coord_map = [[0 for x in range(max_x)] for y in range(max_y)]

    letters = string.ascii_letters
    assert(len(letters)> len(coordinates))

    coord_dict = {letters[i]: coord for i,coord in enumerate(coordinates)}

    boarder_keys = []
    def is_border(p):
        return p[0] == 0 or p[0] == max_x or p[1] == 0 or p[1] == max_y 

    for row_idx in range(max_y):
        print(f'rows calculated: {round(row_idx/(max_y),2)}', flush=True, end="\r")
        for col_idx in range(max_x):
            shortest_dist = float("inf")
            closest_point = []
            for key in coord_dict:
                point = (col_idx,row_idx)
                distance = dist(point,coord_dict[key])
                if distance < shortest_dist:
                    closest_point = [key]
                    shortest_dist = distance
                elif distance == shortest_dist:
                    closest_point.append(distance)
            if len(closest_point) == 1:
                coord_map[row_idx][col_idx] = closest_point[0]
                if is_border(point) and closest_point[0] not in boarder_keys:
                    boarder_keys.append(closest_point[0])
            else:
                coord_map[row_idx][col_idx] = "."

    print(f'rows calculated: {1.00}')
    cnt_dict = {letter:0 for letter in letters}
    for row in coord_map:
        for col in row:
            if col != ".":
                cnt_dict[col] +=1

    filtered_cnt = {k:v for k,v in cnt_dict.items() if k not in boarder_keys}
    return {k:v for k,v in filtered_cnt.items() if v == max(filtered_cnt.values())}


def puzzel2(coordinates):
    max_x = max([val[0] for val in coordinates]) +1
    max_y = max([val[1] for val in coordinates]) +1 
    coord_map = [[0 for x in range(max_x)] for y in range(max_y)]

    letters = string.ascii_letters
    assert(len(letters)> len(coordinates))

    for row_idx in range(max_y):
        print(f'rows calculated: {round(row_idx/(max_y),2)}', flush=True, end="\r")
        for col_idx in range(max_x):
            total_dist = sum(map(
                lambda x: dist(*x),
                list(zip([(col_idx,row_idx) for i in range(len(coordinates))],coordinates))
            ))
            if total_dist <= 10000:
                coord_map[col_idx][row_idx]= 1

    print(f'rows calculated: {1.00}')
    return sum(map(sum,coord_map))

coordinates = sorted([(int(coordinate[0]), int(coordinate[1])) for coordinate in(line.split(",") for line in open("day6_data.txt"))])

print(f'puzzel1: {puzzel1(coordinates)}')
print(f'puzzel2: {puzzel2(coordinates)}')