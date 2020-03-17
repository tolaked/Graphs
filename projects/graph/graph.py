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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exis")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex, visited =None):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
         # Instantiate queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

    # loop over vertices while queue not empty
        while queue.size > 0:
            # dequeue the first vertex
            vertex = queue.dequeue()

         # if current vertex has not been visited
            if vertex not in visited:
                # mark it as visited by printing it out
                # print(vertex)
                visited.add(vertex)

                # add all other neighbor to the back of the queue
                for next_vertex in self.vertices[vertex]:
                    queue.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         # Create new stack and push in starting index
        stack = Stack()
        stack.push(starting_vertex)

        # Store visited vertices
        visited = set()

        while stack.size() > 0:
            # remove the first vertex
            vertex = stack.pop()
          # check if current vertex has not been visited
            if vertex not in visited:
                # mark as visited by add it to visited and printing it out
                # print(vertex)
                visited.add(vertex)
                print(vertex)

                # Add all of it's neighbor's to the top of the stack
                for next_vertex in self.vertices[vertex]:
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if the visited is None
        if visited is None:
            # create a new set for visited
            visited = set()
        
         # add a starting vertex to the visited set
        visited.add(starting_vertex)
        # print the start vertex
        print(starting_vertex)

        # loop over every child vertex in vertices set at the start vertex
        for child_vertex in self.vertices[starting_vertex]:
            # if child vertex is not in visited
            if child_vertex not in visited:
                # do a recursive call to dft_recursive
                # using the child vertex and the current
                #  visited set as arguments
                self.dft_recursive(child_vertex, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # create a queue to hold the vertex ids
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            p = q.dequeue()
            v = p[-1]
            if v not in visited:
                if v == destination_vertex:
                    return p
                visited.add(v)
                for next_vertex in self.get_neighbors(v):
                    new_p = list(p)
                    new_p.append(next_vertex)
                    q.enqueue(new_p)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
       
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            p = stack.pop()
            v = p[-1]
            if v not in visited:
                if v == destination_vertex:
                    return p
                visited.add(v)
                for next_vertex in self.get_neighbors(v):
                    new_p = list(p)
                    new_p.append(next_vertex)
                    stack.push(new_p)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path+[starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for next_vertex in self.get_neighbors(starting_vertex):
            if next_vertex not in visited:
                new_p = self.dfs_recursive(next_vertex, destination_vertex, visited, path)
                if new_p:
                    return new_p
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
