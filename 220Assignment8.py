import sys

def visit(node, height):
    global states
    global input
    maxh = height
    states[node] = "grey"
    for j in input[node]:
        if states[j] == "white":
            maxh = max(maxh, visit(j, height+1))
    states[node] = "black"
    return maxh


while True:
    try:
        order = int(sys.stdin.readline().strip())
    except:
        break

    heights = []
    input = []
    states = []

    for i in range(order):
        input.append(list(map(int, sys.stdin.readline().split())))

    for x in range(int(order)):
        states.append("white")

    for y in range(order):
        if states[y] == "white":
            height = visit(y, 0)
            heights.append(height)
            
    for h in heights:
        print(h, end = " ")
    print()
