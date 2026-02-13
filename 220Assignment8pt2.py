import sys

def visit(node):
    global q
    global states
    global input
    global order
    heights = []
    for n in range(order):
        heights.append(0)
    states[node] = "grey"
    q.append(node)
    heights[node] = 0
    while len(q) > 0:
        next = q.pop(0)
        for j in input[next]:
            if(states[j]) == "white":
                q.append(j)
                heights[j] = heights[next] + 1
                states[j] = "grey"
        states[next] = "black"
    print(max(heights), end = " ")

while True:
    try:
        order = int(sys.stdin.readline().strip())
    except:
        break

    heightsList = []
    input = []
    states = []
    q = []

    for i in range(order):
        input.append(list(map(int, sys.stdin.readline().split())))
        states.append("white")

    for y in range(order):
        if states[y] == "white":
            visit(y)
    
    print()
            
   
