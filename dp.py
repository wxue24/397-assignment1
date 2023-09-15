
def calculateWater(elevationMap: list[int]):
    elevationMapLength = len(elevationMap)
    # max height to the left of the index
    maxLeftHeight = [0] * elevationMapLength
    # max height to the right of the index
    maxRightHeight = [0] * elevationMapLength
    water = 0

    # Calculate the max left height at each index
    for i in range(elevationMapLength):
        if i == 0:
            maxLeftHeight[i] = 0
        else:
            maxLeftHeight[i] = max(maxLeftHeight[i - 1], elevationMap[i - 1])

    # Calculate the max right height at each index
    for i in range(elevationMapLength - 1, -1, -1):
        if i == elevationMapLength - 1:
            maxRightHeight[i] = 0
        else:
            maxRightHeight[i] = max(maxRightHeight[i + 1], elevationMap[i + 1])

    # Add up min of maxRight and maxLeft at each index and subtract elevation at that point
    for i in range(elevationMapLength):
        # add the max of the previously calculated value and 0, in case of negatives
        water += max(min(maxLeftHeight[i], maxRightHeight[i]) - elevationMap[i], 0)

    return water



if __name__ == "__main__":
    # test cases
    if calculateWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6:
        print("passed")
    else:
        print("failed")
