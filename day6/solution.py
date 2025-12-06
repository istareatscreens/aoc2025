import copy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from shared.helper_functions import printSolution1, printSolution2, safeAccessIndex, split2dArrayString, readInputLines

TEST_MODE = False

def solution():

    result = readInputLines(
        str(Path(__file__).resolve().parent),
        TEST_MODE
    )

    numbers = list(map(lambda x: x.split(), result[:len(result)-1]))
    operations = list(map(lambda x: x.split(), result[len(result)-1:]))[0]
    results = []
    for j in range(0, len(numbers[0])):
        results.append(-1)
        for i in range(0, len(numbers)):
            match(operations[j]):
                case '*':
                    if results[j] == -1 :
                        results[j] = int(numbers[i][j])
                    else:
                        results[j] *= int(numbers[i][j])
                case '+':
                    if results[j] == -1 :
                        results[j] = int(numbers[i][j])
                    else:
                        results[j] += int(numbers[i][j])
            
    printSolution1(sum(results))

    numbersWithSpaces = list(map(lambda x: list(x), result[:len(result)-1]))
    operationsWithSpaces = list(map(lambda x: list(x), result[len(result)-1:]))[0]

    newNumbers = []
    results = []
    skipColumn = False
    for j in reversed(range(0, len(numbersWithSpaces[0]))):
        if skipColumn:
            skipColumn = False
            continue
        newNumber = ""
        for i in range(0, len(numbersWithSpaces)):
            newNumber += numbersWithSpaces[i][j] 
        newNumbers.append(newNumber.strip())
        if operationsWithSpaces[j] == "*" or operationsWithSpaces[j] == "+":
            result = -1
            for num in newNumbers:
                match(operationsWithSpaces[j]):
                    case '*':
                        if result == -1 :
                            result = int(num)
                        else:
                            result *= int(num)
                    case '+':
                        if result == -1 :
                            result = int(num)
                        else:
                            result += int(num)
            newNumbers = []
            skipColumn = True
            results.append(result)

    printSolution2(sum(results))

if __name__ == '__main__':
    solution()