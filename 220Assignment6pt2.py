import sys

outList = []
order = sys.stdin.readline().strip()
while(order):
   print(order);
   for y in range(int(order)):
      line = [0] * int(order)
      splitLine = sys.stdin.readline().strip().split()
      for x in range(len(splitLine)):
         line[int(splitLine[x])] = 1
      newLine = ""
      for z in range(int(order)):
        newLine += str(line[z]) + " "
      print(newLine)
   order = sys.stdin.readline().strip()