def evalSeat(seatCode, h, lowerChar):
    l = 0
    for i in range(len(seatCode)):
        m=(l+h)//2
        if seatCode[i]==lowerChar:
            h=m
        else:
            l=m+1
    return l

with open('/Users/master/projects/aoc/2020/5/input.txt') as f:
    lines=f.read().splitlines()
    maxId=0
    for line in lines:
        row = evalSeat(line[0:len(line)-3], 127, 'F')
        col = evalSeat(line[len(line)-3:], 7, 'L')
        seatId=row * 8 + col
        maxId=max(seatId,maxId)
    print(maxId)

