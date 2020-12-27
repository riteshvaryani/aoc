valid=0
with open('/Users/master/projects/aoc/2020/02/input.txt') as f:
    alllines=f.readlines()
    for input in alllines:
        inputSplits=input.split()
        counts = inputSplits[0].split('-')
        index1=int(counts[0])-1
        index2=int(counts[1])-1
        char=inputSplits[1][0]
        pwdlen= len(inputSplits[2])
        word = inputSplits[2]
        if index1 < pwdlen and index1 >=0 and index2 >=0 and index2 < pwdlen and word[index1] == char and word[index2] == char:
            continue
        if (index1 < pwdlen and index1 >=0 and word[index1] == char) or (index2 >=0 and index2 < pwdlen and word[index2] == char):
            valid+=1
print(valid)