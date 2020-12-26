def processPassport(passport):
    reqSplits=passport.split()
    if len(reqSplits) < 7 or len(reqSplits) > 8:
        return 0
    if len(reqSplits) == 8:
        return 1
    codeSet=set()
    for i in reqSplits:
        codeValue=i.split(':')
        codeSet.add(codeValue[0])
    if len(reqSplits) ==7 and 'cid' not in codeSet:
        return 1
    return 0
with open('/Users/master/projects/aoc/2020/4/input.txt') as f:
    lines=f.read().splitlines()
    currPassport=""
    validPassports=0
    for line in lines:
        if line == '':
            validPassports += processPassport(currPassport.strip())
            currPassport=""
            continue
        currPassport+= " " + line
    validPassports += processPassport(currPassport.strip())

print('valid passports ', validPassports)



    