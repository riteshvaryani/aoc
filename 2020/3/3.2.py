with open('/Users/master/projects/aoc/2020/3/input.txt') as f:
    grid=f.read().splitlines()
    rowLen=len(grid)
    colLen=len(grid[0])
    slopes=[[1,1],[1,3],[1,5],[1,7],[2,1]]
    totalTreesHit=[]
    for eachSlope in slopes:
        treesHit=0
        nextRowD=eachSlope[0]
        nextColD=eachSlope[1]
        currrow=0
        currcol=0
        while currrow<rowLen:
            if grid[currrow][currcol]== '#':
                treesHit+=1
            currcol=(currcol +nextColD) % colLen
            currrow = currrow+nextRowD
        totalTreesHit.append(treesHit)
    print('total trees hit ', totalTreesHit)
    total=1
    for i in totalTreesHit:
        total*=i
    print('total trees hit multiplied', total)