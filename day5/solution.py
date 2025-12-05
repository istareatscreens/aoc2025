import copy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.helper_functions import printSolution1, printSolution2, safeAccessIndex, split2dArrayString, readInputLines

TEST_MODE = False

def solution():
    solution_p1 = 0
    solution_p2 = 0

    database = readInputLines(
        str(Path(__file__).resolve().parent),
        TEST_MODE
    )
    ingredientList = []
    freshIngredientRange = []
    for i in range(0,len(database)):
        if len(database[i]) == 0:
            ingredientList = database[i+1:]
            break
        
        uId, lId = database[i].split('-')
        freshIngredientRange.append([int(uId),int(lId)])
    
    for ingredient in ingredientList:
        for i in range(0, len(freshIngredientRange)):
            if freshIngredientRange[i][0] <= int(ingredient) <= freshIngredientRange[i][1]:
                solution_p1 += 1
                break
    
    printSolution1(solution_p1)

    newRanges = copy.deepcopy(freshIngredientRange)
    restart = True
    while restart:
        restart = False
        for i in range(0, len(freshIngredientRange)):
            for j in range(0, len(freshIngredientRange)):
                if i == j:
                    continue
                '''
                    | --- |
                        | --- |
                    
                        | --- |
                    | --- |

                    | --- |
                      |-|
                '''
                # contained
                if withinRange(freshIngredientRange[i][0], freshIngredientRange[j]) and withinRange(freshIngredientRange[i][1], freshIngredientRange[j]):
                    del newRanges[i]
                    restart = True
                    break

                if withinRange(freshIngredientRange[i][0], freshIngredientRange[j]):
                    newRange = [freshIngredientRange[j][0], freshIngredientRange[i][1]]
                    newRanges = list(filter(lambda x: x != freshIngredientRange[i] and x != freshIngredientRange[j], newRanges))
                    newRanges.append(newRange)
                    restart = True
                    break

                if withinRange(freshIngredientRange[i][1], freshIngredientRange[j]):
                    newRange = [freshIngredientRange[i][0], freshIngredientRange[j][1]]
                    newRanges = list(filter(lambda x: x != freshIngredientRange[i] and x != freshIngredientRange[j], newRanges))
                    newRanges.append(newRange)
                    restart = True
                    break
            if restart:
                break
        freshIngredientRange = copy.deepcopy(newRanges)
        
    for i in newRanges:
        solution_p2 += i[1] - i[0] + 1

    printSolution2(solution_p2)

def withinRange(value: int, range: list) -> bool:
    return int(range[1]) >= int(value) and int(range[0]) <= int(value)


if __name__ == '__main__':
    solution()