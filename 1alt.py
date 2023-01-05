def a_star(graph, start, stop, h):
    open_set = set(start)
    closed_set = set()
    g = {start: 0}
    parents = {start: start}

    while open_set:
        # Find the node with the lowest f value
        n = min(open_set, key=lambda x: g[x] + h[x])

        # If the current node is the stop node, reconstruct the path from it to the start node
        if n == stop:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            return path[::-1]

        open_set.remove(n)
        closed_set.add(n)

        # Update the g value of each neighbor of n
        for m, weight in graph[n]:
            if m in closed_set:
                continue
            if m not in open_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
    return None

# Test the function
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}
h = {
             'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0  
}
start = 'A'
stop = 'J'
path = a_star(graph, start, stop, h)
print(path)
