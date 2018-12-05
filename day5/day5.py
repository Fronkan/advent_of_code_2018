import string

def puzzel1(polymer):
    reacted = True
    while reacted:
        #print(len(polymer))
        reacted = False
        last_elem = ""
        for idx, elem in enumerate(polymer):
            #print(f'{last_elem}:{elem}')
            if elem.islower() and elem.upper() == last_elem:
                reacted = True
                rm_idx = idx
                break
            elif elem.isupper() and elem.lower() == last_elem:
                reacted = True
                rm_idx = idx
                break
            last_elem = elem
        if reacted:
            #print(rm_idx)
            #print(f'remmoving: {polymer[rm_idx-1]+polymer[rm_idx]} ')
            polymer = polymer[:rm_idx-1] + polymer[rm_idx+1:]
    #print("DONE!, printing polymer")
    #print(polymer)
    print(f'length of polymer: {len(polymer)}')
    return len(polymer)

def puzzel2(polymer):
    for character in string.ascii_lowercase:
        print(f'Filtering: {character}')
        min_len = float("inf")
        new_poly = "".join(list(filter(lambda e: e.lower() != character ,polymer)))
        pol_length = puzzel1(new_poly)
        if pol_length <= min_len:
            min_len = pol_length
    return min_len



polymer = "".join([line for line in open("day5_data.txt")]).strip()
print(puzzel1(polymer))
print(puzzel2(polymer))