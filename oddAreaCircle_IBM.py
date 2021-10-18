from math import floor, pi, sqrt

def fetchArea(x1,y1,x2,y2):
    distance = floor(sqrt((x1-x2)**2 + (y1-y2)**2))
    radiusOfcircle = floor(distance / (2*(sqrt(2))))
    return floor((pi)*(radiusOfcircle)*(radiusOfcircle))

def findOddNumber(AreaList):
    freqTable = {}
    for i in range(len(AreaList)):
        if AreaList[i] in freqTable.keys():
            freqTable[AreaList[i]] += 1
        else:
            freqTable[AreaList[i]] = 1
    for entry in freqTable:
        if (freqTable[entry] % 2 != 0):
            return entry
    return -1

def findOddCircleArea(coordinatePairs):
    n = len(coordinatePairs)
    for i in range(n):
        if (len(coordinatePairs[i]) > 2):
            print("Invalid Input")
            exit()
    AreaList = []
    for i in range(n-1):
        x1,y1,x2,y2 = coordinatePairs[i][0],coordinatePairs[i][1],coordinatePairs[i+1][0],coordinatePairs[i+1][1]
        AreaList.append(fetchArea(x1,y1,x2,y2))
    ans = findOddNumber(AreaList)
    if ans > 0:
        print(ans)
    else:
        print("Invald Input")
        return

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    coordinatePairs = []
    tempString = ''
    tmp1, tmp2 = 0,0
    for i in range(n):
        tempString = input().split()
        tmpLst = []
        for i in range(len(tempString)):
            tmpLst.append(int(tempString[i]))
        coordinatePairs.append(tmpLst)
    findOddCircleArea(coordinatePairs)