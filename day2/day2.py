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
        ids_one_removed = list(map(lambda c: (c[:char_idx] + c[char_idx+1:id_len], c[char_idx]), ids))
        ids_one_removed = sorted(ids_one_removed, key=lambda pair: pair[0])
        last_id_pair = ("","")
        for id_pair in ids_one_removed:
            if last_id_pair[0] == id_pair[0]:
                #print(f'{last_id_pair}, {id_pair}')
                return id_pair[0]
            else:
                last_id_pair = id_pair

print(f'puzzel 1: {puzzel1()}')
print(f'puzzel 2:{puzzel2()}')