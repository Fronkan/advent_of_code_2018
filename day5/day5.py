import string

def puzzel1_fast(polymer):
    reactions = reactions = [x[0]+x[1] for x in zip(string.ascii_lowercase + string.ascii_uppercase, string.ascii_uppercase+string.ascii_lowercase)]
    last_len = float("inf")
    while len(polymer) != last_len:
        if(polymer == ""):
            return 0
        last_len = len(polymer)
        for reaction in reactions:
            polymer = polymer.replace(reaction,"")
    print(f'length of polymer: {len(polymer)}')
    return len(polymer)

def puzzel2(polymer):
    min_len = float("inf")
    for character in string.ascii_lowercase:
        print(f'Filtering: {character}')
        new_poly = polymer.replace(character, "")
        new_poly = new_poly.replace(character.upper(), "")
        pol_length = puzzel1_fast(new_poly)
        if pol_length <= min_len:
            min_len = pol_length
    return min_len


polymer = "".join([line for line in open("day5_data.txt")]).strip()
print(f'puzzel1: {puzzel1_fast(polymer)}')
print("----------------------------------------")
print(f'puzzel2: {puzzel2(polymer)}')


