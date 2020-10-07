"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
            return self.vertices
        print('Vertix exist')

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            start = queue.dequeue()
            if start not in visited:
                print(start)
                visited.add(start)
                for n in self.get_neighbors(start):
                    queue.enqueue(n)





    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stacky = Stack()
        visited = set()
        stacky.push(starting_vertex)

        while stacky.size() > 0:
            start = stacky.pop()
            if start not in visited:
                visited.add(start)
                print(start)

                for n in self.get_neighbors(start):
                    stacky.push(n)




    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in visited:
            return
        visited.add(starting_vertex)
        print(starting_vertex)
        for n in self.get_neighbors(starting_vertex):
            self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        counter = 0
        while queue.size() > 0:
            new_path = queue.dequeue()
            counter += 1
            print( counter, new_path)
            start_n = new_path[-1]
            if start_n not in visited:
                if start_n is destination_vertex:
                    return new_path
                visited.add(start_n)
                for n in self.get_neighbors(start_n):
                    update_path = list(new_path)
                    update_path.append(n)
                    queue.enqueue(update_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stacky = Stack()
        visited = set()
        stacky.push([starting_vertex])

        while stacky.size() > 0:
            new_path = stacky.pop()
            start = new_path[-1]
            if start == destination_vertex:
                return new_path
            if start not in visited:
                visited.add(start)

                for n in self.get_neighbors(start):
                    updated_path = list(new_path)
                    updated_path.append(n)
                    stacky.push(updated_path)



    def dfs_recursive(self, starting_vertex, destination_vertex, paths=Queue(),visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        path = paths.dequeue()
        # print(path)
        if path == None:
            path = [starting_vertex]


        if path[-1] not in visited:
            visited.add(path[-1])
            for n in self.get_neighbors(path[-1]):
                if n == destination_vertex:
                    path.append(n)
                    return path
                update_path = list(path)
                update_path.append(n)
                paths.enqueue(update_path)
            return self.dfs_recursive(starting_vertex, destination_vertex, paths, visited)

# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)
#
#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)
#
#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)
#
#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)
#
#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))
#
#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))

# g1 = Graph()
# g1.add_vertex(10)
# g1.add_vertex(2)
# g1.add_vertex(6)
# g1.add_edge(10,2)
# g1.add_edge(6,10)
# g1.bft(6)

# arry_1 = [1,2]
# new_arry = list(arry_1)
# new_arry.append(3)
# print(new_arry)