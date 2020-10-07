import sys
sys.path.insert(1, 'z:/LambdaProjects/CS35/Unit2/week5/Graphs/projects/graph')

from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    #input wil not be empty
    #All integers are positive
    #If more than one oldest ancestor, output lowest number
    #no repeated ancestors
    print(starting_node)
    graph = Graph()
    for parent, child in ancestors:
        if child not in graph.vertices:
            graph.vertices[child] = {parent}
            print('in the if',graph.vertices)
        else:
            graph.vertices[child].add(parent)
            print('in the else', graph.vertices)

    stack = []
    stack.append([starting_node])
    parent_track = []
    counter = 0
    while len(stack) > 0:
        print(counter, stack)
        path = stack.pop()
        node = path[-1]
        print(counter, path)
        print('longest',counter, parent_track)
        counter += 1
        if len(path) > len(parent_track):
            parent_track = path
        if node in graph.vertices:
            for parent in graph.vertices[node]:
                newPath = list(path)
                newPath.append(parent)
                stack.append(newPath)

    if parent_track[-1] == starting_node:
        return -1

    else:
        return parent_track[-1]






# graphy = Graph()
# graphy.add_vertex(6)
#
# print(graphy.vertices)

print(earliest_ancestor([(15, 3),(3,9), (2,9), (9,10)], 9))

arry_1 = []
arry_1.append([2])
p = arry_1.pop()
