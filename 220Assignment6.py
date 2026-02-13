import sys

outList = []
order = sys.stdin.readline().strip()
while(order):
   outList.append(order)
   for y in range(int(order)):
      convertedLine = ""
      splitLine = sys.stdin.readline().strip().split()
      for x in range(len(splitLine)):
         if(splitLine[x] == "1"):
            convertedLine += str(x) + " "
      outList.append(convertedLine)
   order = sys.stdin.readline().strip()
for element in outList:
   print(element)