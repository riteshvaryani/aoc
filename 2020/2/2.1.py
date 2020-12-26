valid=0
with open('/Users/master/projects/aoc/2020/2/input.txt') as f:
    alllines=f.readlines()
    for input in alllines:
        inputSplits=input.split()
        counts = inputSplits[0].split('-')
        minCount=int(counts[0])
        maxCount=int(counts[1])
        char=inputSplits[1][0]
        count=0
        
        for i in inputSplits[2]:
            if i ==char:
                count+=1
        if count >= minCount and count <=maxCount:
            valid+=1
print(valid)