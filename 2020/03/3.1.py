with open('/Users/master/projects/aoc/2020/03/input.txt') as f:
    grid=f.read().splitlines()
    currrow=0
    currcol=0
    rowLen=len(grid)
    colLen=len(grid[0])
    trees=0
    while currrow<rowLen:
        if grid[currrow][currcol]== '#':
            trees+=1
        currcol=(currcol +3) % colLen
        currrow = currrow+1
    print('trees hit ', trees)



    