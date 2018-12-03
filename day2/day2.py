def puzzel1():
    with open("day2_data.txt") as f:
        twos = 0
        threes = 0
        for line in f:
            chars = {}
            for char in line:
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
            has3 = False
            has2 = False
            for val in chars.values():
                if val == 2:
                    has2 = True
                elif val == 3:
                    has3 = True
            twos += int(has2)
            threes += int(has3)

    return twos * threes

def puzzel2():
    ids = [line.strip() for line in open("day2_data.txt")]
    id_len = len(ids[0])
    for char_idx in range(id_len):
        ids_one_removed = list(map(lambda c: c[:char_idx] + c[char_idx+1:id_len], ids))
        ids_one_removed = sorted(ids_one_removed)
        last_id = ""
        for cur_id in ids_one_removed:
            if cur_id == last_id:
                return cur_id
            else:
                last_id = cur_id

from itertools import groupby
from functools import reduce 
from operator import mul
def puzzel1_short():
    return mul(*(reduce(lambda p1, p2: (p1[0]+ p2[0], p1[1] + p2[1]) ,map(lambda counts: (2 in counts, 3 in counts) ,map(lambda cur_id:  [len(list(g)) for k,g in groupby(sorted(cur_id))],[line.strip() for line in open("day2_data.txt")])))))


print(f'puzzel 1: {puzzel1()}')
print(f'puzzel 1 - one liner: {puzzel1_short()}')
print(f'puzzel 2: {puzzel2()}')
