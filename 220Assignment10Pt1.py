import sys

def visit(node):
    global q, states, input, order, heights, colors
    states[node] = "grey"
    q.append(node)
    heights[node] = 0
    colors[node] = "blue"
    while len(q) > 0:
        next = q.pop(0)
        for j in input[next]:
            if colors[next] == colors[j]:
                return False
            if states[j] == "white":
                q.append(j)
                heights[j] = heights[next] + 1
                states[j] = "grey"
                if heights[j] % 2 == 0 and colors[j] == "":
                    colors[j] = "blue"
                if heights[j] % 2 == 1 and colors[j] == "":
                    colors[j] = "red"
        states[next] = "black"
    return True

while True:
    try:
        order = int(sys.stdin.readline().strip())
        if order == 0:
            break
    except:
        break

    colors = []
    heights = []
    input = []
    states = []
    q = []
    bipartite = True

    for i in range(order):
        input.append(list(map(int, sys.stdin.readline().split())))
        states.append("white")
        heights.append(0)
        colors.append("")

    for y in range(order):
        if states[y] == "white" and bipartite == True:
            bipartite = visit(y)
            if bipartite == False:
                print(False)
                
    if bipartite == True:
        print(True)

