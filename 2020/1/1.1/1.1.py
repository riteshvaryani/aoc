inputset=set()
with open('/Users/master/projects/aoc/2020/1/input.txt') as f:
    alllines=f.readlines()
    for input in alllines:
        intInput=int(input)
        i=2020-intInput
        if i in inputset:
            print(str(i * intInput))
            exit()
        inputset.add(intInput)