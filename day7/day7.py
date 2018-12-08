
from copy import deepcopy

# ------------------------------------------- Create Node Class -------------------------------------------

class node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            child._add_parent(self)


    def _add_parent(self,parent):
        if parent not in self.parents:
            self.parents.append(parent)


# ------------------------------------------- Built Tree -------------------------------------------

data = [ (word[1], word[7]) for word in (line.split() for line in open("day7_data.txt"))]

#data = [("C","A"), ("C", "F"), ("A","B"), ("A","D"), ("B","E"), ("D","E"), ("F","E")]

roots = None
node_dict = {}
for dep in data:
    if roots is None:
        root = node(dep[0])
        node_dict[root.name] = root
        child = node(dep[1])
        node_dict[child.name] = child
        root.add_child(child)
        roots = [root]
    else:
        if dep[0] not in node_dict:
            new_node = node(dep[0])
            node_dict[new_node.name] = new_node
        else:
            new_node = node_dict[dep[0]]
        
        if dep[1] not in node_dict:
            child = node(dep[1])
            node_dict[child.name] = child
        else:
            child = node_dict[dep[1]]

        new_node.add_child(child)
        if new_node.parents == [] and new_node not in roots:
            roots.append(new_node)

        if child in roots:
            roots.remove(child)


def remove_deps(node):
    for child in node.children:
        child.parents.remove(node)


# ------------------------------------------- Puzzles -------------------------------------------
# Parameter for which puzzle to run, because they are destructive.
puzzel = 2

# ------------------------------------------- puzzle 1: -------------------------------------------
if puzzel == 1:
    res = ""
    while node_dict != {}:
        to_remove = ""
        for key in sorted(node_dict.keys()):
            node = node_dict[key]
            if node.parents == []:
                to_remove = node.name
                break
        if to_remove != "":
            print(f'res: {res}, to_remove: {to_remove}, dict')
            res = res + "".join(sorted(to_remove))
            remove_deps(node_dict[to_remove])
            del node_dict[to_remove]

    print(res)

# ------------------------------------------- puzzle 2: -------------------------------------------
import string
if puzzel == 2:
    num_workers = 5
    idle_workers = num_workers
    working_on = {}
    task_times = {k:60+string.ascii_uppercase.find(k)+1 for k in node_dict.keys()}
    res = ""
    tot_time = 0
    while node_dict != {}:
        to_remove = []
        if idle_workers > 0:
            for key in sorted(node_dict.keys()):
                node = node_dict[key]
                if node.parents == [] and key not in working_on:
                    working_on[key] = task_times[key]
                    idle_workers -= 1
                    if idle_workers == 0:
                        break

        for task in working_on:
            working_on[task] -=1
            if working_on[task] <= 0:
                to_remove.append(task)
                idle_workers += 1

        if to_remove != []:
            #print(f'res: {res}, to_remove: {to_remove}, dict')
            res = res + "".join(sorted(to_remove))
            for task2remove in to_remove:
                remove_deps(node_dict[task2remove])
                del node_dict[task2remove]
                del working_on[task2remove]

        tot_time +=1

    print(tot_time)