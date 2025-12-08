import copy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.helper_functions import printSolution1, printSolution2, safeAccessIndex, split2dArrayString, readInputLines

TEST_MODE = 0

def solution():
    solution_p1 = 0

    laserMap = readInputLines(
        str(Path(__file__).resolve().parent),
        TEST_MODE
    )
    start = laserMap[:1][0]
    laserMap = split2dArrayString(laserMap[1:])

    beamLocations = {}
    beamStartLocation = -1
    for i in range(0, len(start)):
        beamLocations[i] = 0
        if start[i] == 'S':
            beamStartLocation = i
    
    beamLocations[beamStartLocation] = 1
    for i in range(0, len(laserMap)):
        for j in range(0, len(laserMap[0])):
            if laserMap[i][j] == '^' and beamLocations[j] != 0:
                beamLocations[j+1] = 1
                beamLocations[j-1] = 1
                beamLocations[j] = 0
                solution_p1+=1

    printSolution1(solution_p1)
    printSolution2(solve(0, beamStartLocation, laserMap))


MEM = {}
def solve(currentLine,  beamLocation, laserMap):
    key = (currentLine, beamLocation)
    if key in MEM:
        return MEM[key]

    if len(laserMap) - 1 == currentLine:
        return 1
    
    nextLine = currentLine + 1

    if laserMap[currentLine][beamLocation] == '^':
        beamLocationRight = beamLocation + 1
        beamLocationLeft = beamLocation - 1

        result = solve(nextLine, beamLocationRight, laserMap) + solve(nextLine, beamLocationLeft, laserMap)
    else:
        result = solve(nextLine, beamLocation, laserMap)
    

    MEM[key] = result
    return result

if __name__ == '__main__':
    solution()