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
            if states[j] == "white":
                q.append(j)
                heights[j] = heights[next] + 1
                states[j] = "grey"
                if heights[j] % 2 == 0 and colors[j] == "":
                    colors[j] = "blue"
                if heights[j] % 2 == 1 and colors[j] == "":
                    colors[j] = "red"
        states[next] = "black"

def augment(node):
    global input, order, colors, u, v, matches
    states = []
    q = []
    parents = []
    for n in range(order):
        states.append("white")
    states[node] = "grey"
    q.append(node)
    while len(q) > 0:
        next = q.pop(0)
        parents.append(next)
        for j in input[next]:
            if states[j] == "white":
                q.append(j)
                states[j] = "grey"
                if colors[j] == "red" and v[j] == -1:
                    parents.append(j)
                    matches += 1
                    for m in range(len(parents)-1):
                        if m%2 == 0:
                            v[parents[m]] = parents[m+1]
                            u[parents[m+1]] = parents[m]
                            return
        states[next] = "black"

while True:
    try:
        order = int(sys.stdin.readline().strip())
        if order == 0:
            break
    except:
        break

    u = []
    v = []
    colors = []
    heights = []
    input = []
    states = []
    q = []
    matches = 0

    for i in range(order):
        input.append(list(map(int, sys.stdin.readline().split())))
        states.append("white")
        heights.append(0)
        colors.append("")
        u.append(-1)
        v.append(-1)

    for y in range(order):
        if states[y] == "white":
            visit(y)
                
    for b in range(order):
        if(colors[b] == "blue"):
            for c in input[b]:
                if u[b] == -1 and v[c] == -1:
                    u[b] = c
                    v[c] = b
                    matches += 1

    for k in range(order):
        if colors[k] == "blue" and u[k] == -1:
            augment(k)
    print(matches)
            
