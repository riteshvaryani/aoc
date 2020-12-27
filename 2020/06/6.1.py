with open('/Users/master/projects/aoc/2020/06/input.txt') as f:
    lines=f.read().splitlines()
    intersectTemplate={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    intersect=intersectTemplate
    totalSum=0
    for line in lines:
        seen=set()
        if(line==''):
            totalSum+=len(intersect)
            intersect=intersectTemplate
            continue
        for i in line:
            seen.add(i)
        intersect=intersect.intersection(seen)
    totalSum+=len(intersect)
    print(totalSum)
