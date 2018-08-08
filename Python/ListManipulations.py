class ListManipulator:
    def __init__(self, initList):
        try:            
            if type(initList) != list:
                raise TypeError()
            else:
                print("Valid")
        except TypeError:
            print("ListManipulator must be initialized with a list!")


    def __GetMidPoints(self, row):
        midVals = []
        for i in range(len(row)-1):
            midPoint = (row[i] + row[i+1])/2
            midVals.append(midPoint)
        return midVals

    def __InterpolateWithMidpoints(self, valList):
        for row in valList:
            midVals = GetMidPoints(row)
            for i in range(len(midVals)):
                row.insert((2*i) + 1, midVals[i])
        return valList

    def __GetMidRows(self, valList):
        interRows = []
        for i in range(len(valList) - 1):
            newRow = []
            for j in range(len(valList[i])):
                newPoint = (valList[i][j] + valList[i+1][j])/2
                newRow.append(newPoint)
            interRows.append(newRow)
        return interRows

    def __InterpolateWithMidrows(self, valList):
        interRows = GetMidRows(valList)
        for i in range(len(interRows)):
            valList.insert((2*i) + 1, interRows[i])
        return valList
