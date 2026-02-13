import sys

def visit(node):
    global states
    global input
    states[node] = "grey"
    for j in input[node]:
        if states[j] == "white":
            visit(j)
    states[node] = "black"

while True:
    try:
        order = int(sys.stdin.readline().strip())
        if(order == 0):
            break
    except:
        break

    input = []
    states = []
    weakTrees = 0

    for i in range(order):
        input.append(list(map(int, sys.stdin.readline().split())))

    for a in range(order):
        for b in range(len(input[a])):
            if a not in input[input[a][b]]:
                input[input[a][b]].append(a)

    for x in range(int(order)):
        states.append("white")

    for y in range(order):
        if states[y] == "white":
            visit(y)
            weakTrees = weakTrees + 1
    print(weakTrees)