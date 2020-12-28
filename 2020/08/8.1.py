globalacc=0
with open('/Users/master/projects/aoc/2020/08/input.txt') as f:
    lines=f.read().splitlines()
counter=0
instructionscompleted=set()
while True:

for line in lines:
    bagsplits=line.split('contain')
    parentBagColor=bagsplits[0][0:bagsplits[0].index('bag')].strip()
    bagsplits[1]=bagsplits[1][0:len(bagsplits[1])-1]
    childBags=bagsplits[1].split(',')
    for eachChild in childBags:
        eachChild=eachChild[0:eachChild.index('bag')].strip()
        childColor=eachChild.split(' ',1)[1]
        if childColor in colorMap:
            colorMap[childColor].append(parentBagColor)
        else:
            colorMap[childColor]=[parentBagColor]

uniqueColors=set()

currentColorQ=['shiny gold']
while(len(currentColorQ) >0):
    popped=currentColorQ.pop(0)
    if popped in colorMap:    
        for i in colorMap[popped]:
            uniqueColors.add(i)
            currentColorQ.append(i)
print(len(uniqueColors))
print(uniqueColors)