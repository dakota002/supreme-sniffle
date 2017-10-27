def GetMidPoints(row):
    midVals = []
    for i in range(len(row)-1):
        midPoint = (row[i] + row[i+1])/2
        midVals.append(midPoint)
    return midVals

def InterpolateWithMidpoints(valList):
    for row in valList:
        midVals = GetMidPoints(row)
        for i in range(len(midVals)):
            row.insert((2*i) + 1, midVals[i])
    return valList

def GetMidRows(valList):
    interRows = []
    for i in range(len(valList) - 1):
        newRow = []
        for j in range(len(valList[i])):
            newPoint = (valList[i][j] + valList[i+1][j])/2
            newRow.append(newPoint)
        interRows.append(newRow)
    return interRows

def InterpolateWithMidrows(valList):
    interRows = GetMidRows(valList):
    for i in range(len(interRows)):
        valList.insert((2*i) + 1, interRows[i])
    return valList
