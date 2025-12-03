import math;

def findMaxBatteries(batteryList: list, lBound, uBound)-> dict:
    largestBattery = {"max": int(batteryList[lBound]), "index": lBound}
    if lBound  < len(batteryList) - uBound:
        for i in range(lBound + 1, len(batteryList) - uBound):
            currentBattery = int(batteryList[i])
            if largestBattery["max"] < currentBattery:
                largestBattery["max"] = currentBattery
                largestBattery["index"] = i
    return largestBattery;


def day2():
    solution_p1 = 0

    batteryBanks = []
    with open('./input/input', 'r') as f:
        for line in f:
            batteryBanks.append(line.rstrip('\n'));
    
    solution_p1 = 0;
    solution_p2 = 0
    for batteryBank in batteryBanks:
        batteriesInBank = list(batteryBank)

        # Solution 1
        largestBatteryOne = {"max": int(batteriesInBank[0]), "index": 0 }
        for i in range(1, len(batteriesInBank) - 1):
            currentBattery = int(batteriesInBank[i]); 
            if largestBatteryOne["max"] < currentBattery :
                largestBatteryOne["max"] = currentBattery
                largestBatteryOne["index"] = i
        
        indexAfterLargestBattery = largestBatteryOne["index"] + 1
        largestBatteryTwo = {"max": int(batteriesInBank[indexAfterLargestBattery]), "index": indexAfterLargestBattery}
        if indexAfterLargestBattery < len(batteriesInBank) - 1:
            for i in range(indexAfterLargestBattery, len(batteriesInBank)):
                currentBattery = int(batteriesInBank[i])
                if largestBatteryTwo["max"] < currentBattery:
                    largestBatteryTwo["max"] = currentBattery
                    largestBatteryTwo["index"] = i
        
        solution_p1 +=int(str(largestBatteryOne['max']) + str(largestBatteryTwo['max']))

        # Solution 2
        lowerBound = 0 
        upperBound = 11
        result = ""
        for _ in range(0, 12):
            curr = findMaxBatteries(
                batteriesInBank,
                lowerBound,
                upperBound
            )
            result += str(curr["max"])
            lowerBound = curr["index"] + 1
            upperBound-=1
        solution_p2 += int(result)
        result = ""

    print("🎄 P1 Solution: " + str(solution_p1))
    print("🎄 P2 Solution: " + str(solution_p2))

if __name__ == '__main__':
    day2()