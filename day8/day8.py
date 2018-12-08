

# ------------------------------------------- Create Node class -------------------------------------------
class Node:
    def __init__(self, num_children,num_meta_data):
        self.num_children = num_children
        self.num_meta_data = num_meta_data
        self.meta_data = []
        self.children = []

    def add_meta_data(self, number):
        self.meta_data.append(number)
        assert(len(self.meta_data) <= self.num_meta_data)

    def add_child(self, node):
        self.children.append(node)
        assert(len(self.children) <=self.num_children)

    def __repr__(self):
        return f'({self.num_children}, {self.num_meta_data})'

    def __str__(self):
        return self.__repr__()


# ------------------------------------------- Load Data -------------------------------------------
with open("day8_data.txt") as f:
    raw = f.read()
    data = list(map(int, raw.strip().split()))

#data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]



# ------------------------------------------- Build tree -------------------------------------------
node_stack = []
data_stack = []

STATE_CHILDREN = "num_children"
STATE_NUM_META = "num_meta_data"
STATE_READ_META = "meta_data"

state= STATE_CHILDREN

cur_node = None
root = None
for number in data:
    #print(f'number: {number}, State: {state}, stack: {node_stack}')
    if state == STATE_CHILDREN:
        data_stack.append(number)
        state = STATE_NUM_META
    
    elif state == STATE_NUM_META:
        num_children = data_stack.pop()
        cur_node = Node(num_children, number)

        if len(node_stack) >0:
            node_stack[-1].add_child(cur_node)

        if cur_node.num_children > 0:
            node_stack.append(cur_node)
            state = STATE_CHILDREN
        else:
            state = STATE_READ_META

    elif state == STATE_READ_META:
        cur_node.add_meta_data(number)
        if len(cur_node.meta_data) == cur_node.num_meta_data:
            if len(node_stack) > 0: 
                peek_node = node_stack[-1]
                if len(peek_node.children) < peek_node.num_children:
                    state = STATE_CHILDREN
                    cur_node = None
                else:
                    cur_node = node_stack.pop()
            else:
                #print("No more nodes")
                #print(cur_node)
                root = cur_node

# ------------------------------------------- Puzzle 1 -------------------------------------------
def calc_meta_tree(node):
    if node.children == []:
        return sum(node.meta_data)
    else:
        return sum(node.meta_data) + sum(map(calc_meta_tree, node.children))

print(f'Puzzle 1: {calc_meta_tree(root)}')


# ------------------------------------------- Puzzle 2 -------------------------------------------
def calc_value(node):
    if node.children == []:
        return sum(node.meta_data)
    else:
        references = list(filter(lambda ref: ref <= len(node.children),node.meta_data))
        children = [node.children[ref-1] for ref in references]
        return sum(map(calc_value, children)) 

print(f'Puzzle 2: {calc_value(root)}')