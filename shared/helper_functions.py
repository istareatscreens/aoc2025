import os

ACCESS_ERROR = "ACCESS_ERROR"

def readInputLines(path: str, test: bool) -> list|str:
    if test:
        print("TEST MODE ON")
    input_lines = []
    filename = 'test' if test else 'input'
    file_path = os.path.join(path, 'input', filename)
    with open(file_path, 'r') as f:
        for line in f:
            input_lines.append(line.rstrip('\n'))
    return input_lines if len(input_lines) > 1 else input_lines[0]

def split2dArrayString(array: list) -> list:
    return list(map(lambda x: list(x), array))

def safeAccessIndex(indices: list, array: list):
    result = array
    try:
        for i in indices:
            if i < 0:
                return ACCESS_ERROR
            result = result[i] 
    except:
        return ACCESS_ERROR
    return result
    

def printSolution1(result) -> None:
    print("🎄 P1 Solution: " + str(result))

def printSolution2(result) -> None:
    print("🎄 P2 Solution: " + str(result))