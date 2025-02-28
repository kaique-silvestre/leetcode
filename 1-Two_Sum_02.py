
def TwoSum(target, array):
    # dict{NumbertoSum: PositionOfTheLockedOne}
    IndexDict = dict()
    for index, num in enumerate(array):
        if num in IndexDict:
            return IndexDict[num], index
        result = target - num 
        IndexDict[result] = array.index(num)
    return "There's no such sum that's equal to the target"




l1 = [2, 2, 7, 15, 7, 11, 7]


print(TwoSum(9, l1))