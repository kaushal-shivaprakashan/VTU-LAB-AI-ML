graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': []
     
}
    
h = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    'G': 1,
}

start = 'A'
stop = 'G'

open_set = set(start) 
closed_set = set()

g = {}
g[start] = 0

parents = {}
parents[start] = start


while len(open_set) > 0:
    n = None

    #node with lowest f() is found
    for v in open_set:
        if n == None or g[v] + h[v] < g[n] + h[n]:
            n = v

    if n == None:
        print('Path does not exist!')
        break

    # if the current node is the stop_node
    # then we begin reconstructin the path from it to the start_node
    if n == stop:
        path = []

        while parents[n] != n:
            path.append(n)
            n = parents[n]

        path.append(start)

        path.reverse()

        print('Path found: {}'.format(path))
        break
    
    for (m, weight) in graph[n]:
        #nodes 'm' not in first and last set are added to first
        #n is set its parent
        if m not in open_set and m not in closed_set:
            open_set.add(m)
            parents[m] = n
            g[m] = g[n] + weight


        #for each node m,compare its distance from start i.e g(m) to the
        #from start through n node
        else:
            if g[m] > g[n] + weight:
                #update g(m)
                g[m] = g[n] + weight
                #change parent of m to n
                parents[m] = n

                #if m in closed set,remove and add to open
                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)
    
    open_set.remove(n)
    closed_set.add(n)
