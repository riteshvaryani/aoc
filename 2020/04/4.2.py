def processPassport(passport):
    reqSplits=passport.split()
    if len(reqSplits) < 7 or len(reqSplits) > 8:
        return 0
    codeSet=set()
    for i in reqSplits:
        codeValue=i.split(':')
        if codeValue[0] =='byr':
            if int(codeValue[1])<1920 or int(codeValue[1]) > 2002:
                return 0
        elif codeValue[0] =='iyr':
            if int(codeValue[1])<2010 or int(codeValue[1]) > 2020:
                return 0
        elif codeValue[0] =='eyr':
            if int(codeValue[1])<2020 or int(codeValue[1]) > 2030:
                return 0
        elif codeValue[0] =='hgt':
            if not codeValue[1].endswith('cm') and not codeValue[1].endswith('in'):
                return 0
            val=int(codeValue[1][0:len(codeValue[1])-2])
            if codeValue[1].endswith('cm') and (val < 150 or val > 193):
                return 0
            if codeValue[1].endswith('in') and (val < 59 or val > 76):
                return 0
        elif codeValue[0] =='hcl':
            if not codeValue[1].startswith('#') or len(codeValue[1]) !=7:
                return 0
            try:
                int(codeValue[1][1:],16)
            except ValueError:
                return 0
        elif codeValue[0] =='ecl':
            colorSet={'amb','blu','brn','gry','grn','hzl','oth'}
            if codeValue[1] not in colorSet:
                return 0
        elif codeValue[0] =='pid':
            if len(codeValue[1]) !=9:
                return 0
            try:
                int(codeValue[1])
            except ValueError:
                return 0
        codeSet.add(codeValue[0])
    if len(reqSplits) ==7 and 'cid' not in codeSet:
        return 1
    if len(reqSplits) ==8:
        return 1
    return 0
with open('/Users/master/projects/aoc/2020/04/input.txt') as f:
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