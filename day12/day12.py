
# ---------------------------------------- Rule representation ----------------------------------------
class Rule:
    """
        Rule object, has a cause which is when the rule is triggered and the effect,
        which is the effect of the rule when triggered
    """
    def __init__(self, cause, effect):
        self.cause = cause.strip()
        self.effect = effect.strip()

    def __repr__(self):
        return f'{self.cause} => {self.effect}'

def parse_rule(symbols):
    """
        Parse the rules into Rule objects
    """
    split_line = symbols.split("=>")
    cause = split_line[0]
    effect = split_line[1]
    return Rule(cause, effect)


# ---------------------------------------- Calc Score----------------------------------------
def calc_score(state, padding_len):
    """
        Calculate the score of a state, based on the amount of padding used around
        the inital_state data.
    """
    tot = 0
    val = -padding_len
    for plant in state:
        
        if plant == "#":
            tot += val
        val += 1
    return tot


# ---------------------------------------- Simulation ----------------------------------------

def simulate(initial_state, rules,padding_len, num_generations):
    """
        Function running the simulation of the plants.
        Quits after finding a stable moving state.

        Inspecting the state over multiple iterations it seems like we reach a 
        stable moving state. Such that we only have plants moving right some amount of steps
        between each iterations. Therefore we can check if the diff between last score and current score
        stays constant over multiple iteration. Indicating a stable moving state and at that point it is possible
        to just calculate the end score. This means we do not need to make 50 billion iteration, which is nice. 
    """
    state = initial_state
    stable_diffs = 0
    last_diff = 0
    last_score = calc_score(initial_state, padding_len)
    for gen in range(1, num_generations+1):
        new_state = ["." for i in range(len(state))]
        for i in range(2,len(state)-1-2):
            for rule in rules:
                if rule.cause == state[i-2:i+3]:
                    new_state[i] = rule.effect
                    break
        state = "".join(new_state)

        # Implementation of stable moving state check
        score = calc_score(state,padding_len)
        diff = score-last_score
        if diff == last_diff:
            stable_diffs += 1
            if stable_diffs == 5:
                return score + (num_generations - gen)*diff
        else:
            stable_diffs = 0

        last_score = score
        last_diff = diff

    return score



# ---------------------------------------- Read Data ----------------------------------------
padding_len = 5000
rules = []
with open("day12_data.txt") as f:
    initial_state  ="."*padding_len + f.readline().split()[-1] + "."*padding_len
    for line in f:
        if len(line) > 4:
            rules.append(parse_rule(line))

# ---------------------------------------- Show Puzzle Results ----------------------------------------
print(f'Puzzle 1: {simulate(initial_state,rules,padding_len, 20)}')
print(f'Puzzle 2: {simulate(initial_state,rules,padding_len, 50000000000)}')
