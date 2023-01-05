def computeMinimumCostChildNodes(n, h, g):
    minCost = 0
    
    costToChildNode = {}
    costToChildNode[minCost] = []
    
    flag = True
    for nodeInfoTupleList in g[n]:
        cost = 0
        nodeList = []
        
        for c, w in nodeInfoTupleList:
            cost = cost + h[c] + w
            nodeList.append(c)
            
        if flag == True:
            minCost = cost
            costToChildNode[minCost] = nodeList
            flag=False
            
        else:
            if minCost > cost:
                minCost = cost
                costToChildNode[minCost] = nodeList
                
    return minCost, costToChildNode[minCost]
def aostar(status, h, graph, solutionGraph, n, backTracking):
    
    print("HEURISTIC VALUES :", h)
    print("SOLUTION GRAPH :", solutionGraph)
    print("PROCESSING NODE :", n)
    print("-----------------------------------------------------------------------------------------")
        
    if status[n] >= 0:
        minCost, childNodeList = computeMinimumCostChildNodes(n, h, graph)
        print(minCost, childNodeList)
        
        h[n] = minCost
        status[n] = len(childNodeList)
        solved = True
        
        for childNode in childNodeList:
            parent[childNode] = n
            if status[childNode] != -1:
                solved = solved & False
        
        if solved==True:
            status[n] = -1
            solutionGraph[n] = childNodeList
        
        if n != start:
            aostar(status, h, graph, solutionGraph, parent[n], True)
            
        if backTracking == False:
            for childNode in childNodeList:
                status[childNode] = 0
                aostar(status, h, graph, solutionGraph, childNode, False)
h = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}

graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]],
    'I': [],
    'J': []
}

start = 'A'

parent = {}

status = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0
}

solution = {}

aostar(status, h, graph, solution, start, False)

print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", start)
print("------------------------------------------------------------")
print(solution)
print("------------------------------------------------------------")
