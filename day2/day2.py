import math;

def checkForSymmetry(num: int) -> bool:
    # Find all divisors
    divisors = []
    numLength = len(str(num)) 

    # oof
    if numLength == 1:
        return False

    for j in range(1, math.ceil(numLength/2)+1):
        if numLength % j == 0: 
            divisors.append(j)
    divisors.reverse()

    # Check Symmetry using divisors
    #print("num : "+ str(num) +" divisors: " + str(divisors))
    for divider in divisors:
        num_string = str(num)
        prev = num_string[:divider]
        num_string = num_string[divider:]
        symmetric = True
        while num_string != "":
            cur = num_string[:divider]
            num_string = num_string[divider:]
            if cur != prev:
                symmetric = False
                break;
            prev = cur
        if symmetric:
            print(str(num) + " " + str(divider))
            return True

    
    return False

def day2():
    solution_p1 = 0

    id_ranges = []
    with open('./input/input', 'r') as f:
        line = f.readline()
        ranges = line.split(',')
        for rangeString in ranges:
            id_ranges.append(rangeString.split('-'))
        

    for rangeBounds in id_ranges:
        for i in range(int(rangeBounds[0]),(int(rangeBounds[1]) + 1)):
            num_string = str(i)
            if len(num_string) % 2 != 0:
                continue

            half_length = len(str(i)) // 2
            if num_string[:half_length] == num_string[half_length:]:
                solution_p1 += i
    print("P1 Solution: " + str(solution_p1))


    solution_p2 = 0
    for rangeBounds in id_ranges:
        for num in range(int(rangeBounds[0]),(int(rangeBounds[1]) + 1)):
            if checkForSymmetry(num):
                # print("Num: " + str(num) + " + Sol: " + str(solution_p2) + " = " + str(solution_p2 + num))
                solution_p2 += num

    print("P2 Solution: " + str(solution_p2))


if __name__ == '__main__':
    day2()