import re
from pprint import pprint
# Puzzel 1
def create_rect(rect):
    rect_dict = {
        "id": rect[0],
        "left": int(rect[1]),
        "right": int(rect[1]) + int(rect[3]),
        "top": int(rect[2]),
        "bottom": int(rect[2]) + int(rect[4]),
        "width": int(rect[3]),
        "height": int(rect[4]),
    }
    simple_rect = {}
    simple_rect["id"] = rect_dict["id"]
    simple_rect["min"] = {"x": rect_dict["left"], "y": rect_dict["top"]}
    simple_rect["max"] = {"x": rect_dict["right"], "y": rect_dict["bottom"]}
    return simple_rect


def calc_overlapp(rect1, rect2):
    overlap_x = max(
        0, 
        min(rect1["max"]["x"], rect2["max"]["x"]) - max(rect1["min"]["x"], rect2["min"]["x"])
    )
    overlap_y = max(
        0, 
        min(rect1["max"]["y"], rect2["max"]["y"]) - max(rect1["min"]["y"], rect2["min"]["y"])
    )
    return overlap_x * overlap_y

def calc_overlaping_rect(rect1, rect2):
    overlap_rect = {}
    if calc_overlapp(rect1, rect2) > 0:
        overlap_rect["min"] = {
            "x": max(rect1["min"]["x"], rect2["min"]["x"]),
            "y": max(rect1["min"]["y"], rect2["min"]["y"])
        }
        overlap_rect["max"] = {
            "x": min(rect1["max"]["x"], rect2["max"]["x"]),
            "y": min(rect1["max"]["y"], rect2["max"]["y"])
        }
        return overlap_rect
    else:
        return None

def puzzel1():
    intersects = [[0 for x in range(1000)] for y in range(1000)]
    data = [create_rect(re.findall(r"[\d']+", line)) for line in open("day3_data.txt")]
    tot_overlap = 0
    for rect1_idx in range(len(data)):
        for rect2_idx in range(rect1_idx+1, len(data)):
            overlap = calc_overlaping_rect(data[rect1_idx], data[rect2_idx])
            if overlap is not None:
                for y in range(overlap["min"]["y"],overlap["max"]["y"]):
                    for x in range(overlap["min"]["x"],overlap["max"]["x"]):
                        intersects[x][y] = 1
    return sum(list(map(sum, intersects)))




print(puzzel1())


# puzzel 2 
def puzzel2():
    intersects = [[0 for x in range(1000)] for y in range(1000)]
    data = [create_rect(re.findall(r"[\d']+", line)) for line in open("day3_data.txt")]
    tot_overlap = 0

    for rect1_idx in range(len(data)):
        collided = False
        for rect2_idx in range(len(data)):
            if rect2_idx == rect1_idx:
                continue
            overlap = calc_overlaping_rect(data[rect1_idx], data[rect2_idx])
            if overlap is not None:
                collided = True
                break
        if not collided:
            return data[rect1_idx]


print(puzzel2())