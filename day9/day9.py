class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value 
        if prev_node is not None:
            self.prev = prev_node
        else:
            self.prev = self
        if next_node is not None:
            self.next = next_node
        else:
            self.next = self

    def __repr__(self):
        return f'({self.value}, {self.prev.value}, {self.next.value})'


class Marble_buffer:
    def __init__(self, num_players):
        self.next_marble = 1
        self.players = [0 for i in range(num_players)]
        self.cur_player = 0
        self.current = Node(0)

    def place_next(self):

        if self.next_marble %23 == 0:
            self.player_score()
        else:
            new_node = Node(self.next_marble, self.current.next, self.current.next.next)
            self.current.next.next.prev = new_node
            self.current.next.next = new_node
            self.current = new_node
        self.next_player()
        self.next_marble += 1

    def player_score(self):
        self.players[self.cur_player] += self.next_marble

        for i in range(7):
            self.current = self.current.prev
        self.players[self.cur_player] += self.delete_current()
        
    def delete_current(self):
        val = self.current.value
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current = self.current.next
        return val

    def next_player(self):
        self.cur_player = (self.cur_player +1) % len(self.players)



def play_marble(num_players, last_marble):
    game = Marble_buffer(num_players)

    while game.next_marble <= last_marble:
        game.place_next()

    return max(game.players)



with open("day9_data.txt") as f:
    raw = f.read()
    data = [int(word) for word in raw.split() if word.isdigit()]
    num_players = data[0]
    last_marble = data[1]

print(f'Puzzle 1: {play_marble(num_players,last_marble)}')
print(f'Puzzle 2: {play_marble(num_players,last_marble*100)}')