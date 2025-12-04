import copy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.helper_functions import printSolution1, printSolution2, safeAccessIndex, readInputLines

TEST_MODE = False

def accessAndRemoveRolls(paperMap) -> dict:
    removed = 0
    newMap = copy.deepcopy(paperMap)
    for i in range(0, len(paperMap)):
        for j in range(0, len(paperMap[0])):
            if paperMap[i][j] != "@":
                continue
            count = 0
            for indices in [
                [i+1, j-1], [i+1,j], [i+1,j+1],
                [i, j-1],            [i, j+1],
                [i-1, j-1], [i-1,j], [i-1,j+1]
            ]:
                if safeAccessIndex(indices, paperMap) == "@":
                    count+=1

            if count < 4:
                removed += 1
                newMap[i][j] = "x"

    return {"removed": removed, "paperMap": newMap}

def solution():
    solution_p1 = 0
    solution_p2 = 0

    paperMap = readInputLines(
        str(Path(__file__).resolve().parent),
        TEST_MODE
    )

    for i in range(0, len(paperMap)):
        for j in range(0, len(paperMap[0])):
            if paperMap[i][j] != "@":
                continue
            count = 0
            for indices in [
                [i+1, j-1], [i+1,j], [i+1,j+1],
                [i, j-1],            [i, j+1],
                [i-1, j-1], [i-1,j], [i-1,j+1]
            ]:
                if safeAccessIndex(indices, paperMap) == "@":
                    count+=1

            if count < 4:
                solution_p1 += 1
            
    printSolution1(solution_p1)

    paperMap = list(map(lambda x: list(x), paperMap))
    solution_p2 = 0
    while True:
        result = accessAndRemoveRolls(paperMap)
        if result["removed"] == 0:
            break
        solution_p2 += result["removed"]
        paperMap = result["paperMap"]

    printSolution2(solution_p2)

if __name__ == '__main__':
    solution()