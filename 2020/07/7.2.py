def getTotalBags(color):
    if color not in colorMap:
        return 1
    insideColors=colorMap[color]
    total=1
    for colorQuant in insideColors:
        colorQuantSplit=colorQuant.split(':')
        total+=int(colorQuantSplit[1]) * getTotalBags(colorQuantSplit[0])
    return total
with open('/Users/master/projects/aoc/2020/07/input.txt') as f:
    lines=f.read().splitlines()
    colorMap={}
    for line in lines:
        bagsplits=line.split('contain')
        parentBagColor=bagsplits[0][0:bagsplits[0].index('bag')].strip()
        bagsplits[1]=bagsplits[1][0:len(bagsplits[1])-1]
        childBags=bagsplits[1].split(',')
        for eachChild in childBags:
            eachChild=eachChild[0:eachChild.index('bag')].strip()
            if eachChild == 'no other':
                continue
            childColorQuant=eachChild.split(' ',1)
            childQuant=childColorQuant[0].strip()
            childColor=childColorQuant[1].strip()
            if parentBagColor in colorMap:
                colorMap[parentBagColor].append(childColor+':'+childQuant)
            else:
                colorMap[parentBagColor]=[childColor+':'+childQuant]
m=getTotalBags('shiny gold')
print(m-1)
