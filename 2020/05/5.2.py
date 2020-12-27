def evalSeat(seatCode, h, lowerChar):
    l = 0
    for i in range(len(seatCode)):
        m=(l+h)//2
        if seatCode[i]==lowerChar:
            h=m
        else:
            l=m+1
    return l

with open('/Users/master/projects/aoc/2020/05/input.txt') as f:
    lines=f.read().splitlines()
    seatIdList=[]
    for line in lines:
        row = evalSeat(line[0:len(line)-3], 127, 'F')
        col = evalSeat(line[len(line)-3:], 7, 'L')
        seatId=row * 8 + col
        seatIdList.append(seatId)
    seatIdList = sorted(seatIdList)
    for i in range(1, len(seatIdList)):
        if seatIdList[i]- seatIdList[i-1] >1:
            print(seatIdList[i]-1)
            break

