inputset=set()
with open('/Users/master/projects/aoc/2020/01/input.txt') as f:
    alllines=f.readlines()
   
len = len(alllines)
for index1 in range(len):
    intInput1= int(alllines[index1])
    for index2 in range(len):
        if (index1 ==index2):
            continue
        intInput2= int(alllines[index2])
        i=2020-(intInput1+intInput2)
        if i in inputset:
            print(str(i * intInput1 * intInput2))
            exit()
        inputset.add(intInput2)


    
