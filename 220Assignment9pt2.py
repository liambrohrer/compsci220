import sys

def visit(node, graph):
    global states
    global done
    global time
    states[node] = "grey"
    for j in graph[node]:
        if states[j] == "white":
            time += 1
            visit(j, graph)
    states[node] = "black"
    done[node] = time
    time += 1

while True:
    try:
        order = int(sys.stdin.readline().strip())
        if(order == 0):
            break
    except:
        break
    
    graph = []
    states = []
    done = []
    time = 0

    for i in range(order):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for x in range(order):
        states.append("white")
        done.append(0)

    for y in range(order):
        if states[y] == "white":
            time += 1
            visit(y, graph)


    reverseGraph = []
    scc = 0

    for z in range(order):
        row = []
        reverseGraph.append(row)
        states[z] = "white"

    for a in range(order):
        for b in range(len(graph[a])):
            reverseGraph[graph[a][b]].append(a)

    lastFinished = sorted(range(order), key=lambda x: done[x], reverse=True)
        
    for c in range(order):
        if states[lastFinished[c]] == "white":
            scc += 1
            visit(lastFinished[c], reverseGraph)
    print(scc)