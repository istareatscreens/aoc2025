import copy
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.helper_functions import print2d, printSolution1, printSolution2, safeAccessIndex, split2dArrayString, readInputLines

class Circuit:

    def __init__(self, member):
        self.members = [member]

    def count(self):
        return len(self.members)
    
    def add(self, key):
        if key not in self.members:
            self.members.append(key)
    
    def get(self):
        return self.members
    
    def merge(self, circuit):
        for item in circuit.get():
            self.add(item)
        return self

def solution(testMode: int):
    solution_p1 = 0
    solution_p2 = 0

    boxCoords = readInputLines(
        str(Path(__file__).resolve().parent),
        testMode
    )
    boxCoords = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), boxCoords))

    distances = []
    for i in range(len(boxCoords)):
        for j in range(i + 1, len(boxCoords)):
            distances.append(
                (euclideanDistance(boxCoords[i], boxCoords[j]), (i, j))
            )
    
    distances = sorted(distances, key=lambda item: item[0])

    circuits = {}
    for boxCoord in boxCoords:
        circuits[createKey(boxCoord)] = Circuit(createKey(boxCoord))
    
    steps = 10 if testMode else 1000
    for count, (_, (i, j)) in enumerate(distances):
        if count == steps:
            rawCircuitsArray = list(map(lambda x: x[1], circuits.items()))
            rawCircuitsArray = list(set(rawCircuitsArray))
            rawCircuitsArray = list(map(lambda x: x.get(), rawCircuitsArray))
            rawCircuitsCount = list(map(lambda x: len(x), rawCircuitsArray))
            rawCircuitsCount.sort()
            #print2d(rawCircuitsArray)
            #print(rawCircuitsCount)
            solution_p1 = rawCircuitsCount[-1] * rawCircuitsCount[-2] * rawCircuitsCount[-3]
            printSolution1(solution_p1)
        keyI = createKey(boxCoords[i]) 
        keyJ = createKey(boxCoords[j]) 
        
        if circuits[keyI] is circuits[keyJ]:
            continue

        newCircuit = circuits[keyI].merge(circuits[keyJ])
        for key in newCircuit.get():
            circuits[key] = newCircuit

        rawCircuitsArray = list(map(lambda x: x[1], circuits.items()))
        rawCircuitsArray = list(set(rawCircuitsArray))
        rawCircuitsArray = list(map(lambda x: x.get(), rawCircuitsArray))
        #print(rawCircuitsArray)
        #print(len(rawCircuitsArray))
        if len(rawCircuitsArray) == 1:
            solution_p2 = [int(keyI.split(',')[0]), int(keyJ.split(',')[0])]
            break
    
    #print(solution_p2)
    printSolution2(solution_p2[0]*solution_p2[1])

def createKey(arr: list) -> str:
    return ','.join(list(map(lambda x: str(x), arr)))


def euclideanDistance(coord1, coord2) -> float:
    return math.sqrt(
        (int(coord2[0]) - int(coord1[0]))**2 +
        (int(coord2[1]) - int(coord1[1]))**2 + 
        (int(coord2[2]) - int(coord1[2]))**2
    )

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 0
    solution(int(arg))