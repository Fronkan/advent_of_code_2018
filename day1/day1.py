
def puzzel1():
    freq = 0
    with open("day1_data.txt") as f:
        for line in f:
            freq += int(line)
    print(freq)

def puzzel2():
    with open("day1_data.txt") as f:
        changes = [int(line) for line in f]
    
    same_freq_found = False
    freqs = [changes[0]]
    freq = changes[0]
    idx = 1
    while not same_freq_found:
        if idx == len(changes):
            idx = 0
        freq += changes[idx]
        if freq in freqs:
            print(freq)
            same_freq_found = True
            break
        else:
            freqs.append(freq)
            idx += 1

def puzzel1_short_solution():
    print(sum([int(line) for line in open("day1_data.txt")]))


if __name__ == "__main__":
    puzzel1()
    puzzel1_short_solution()
    puzzel2()