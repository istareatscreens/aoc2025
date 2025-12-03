def day1():
    solution_p1 = solution_p2 = 0
    with open('./input/input', 'r') as f:
        position = previous_position = 50
        for line in f:
            line = line.rstrip('\n');
            rotation = int(line[1:])
            print(line, line[0], rotation)            

            match line[0]:
                case 'L':
                    position -= rotation
                case 'R':
                    position += rotation
            
            number_of_times_crossed_zero = abs(int( position / 100))
            if position <= 0 and previous_position != 0:
                number_of_times_crossed_zero += 1;
            
            solution_p2 += number_of_times_crossed_zero

            position = position % 100  
            if position == 0:
                solution_p1 = solution_p1 + 1;

            previous_position = position
            
        print("P1 Solution: " + str(solution_p1))
        print("P2 Solution: " + str(solution_p2))

if __name__ == '__main__':
    day1()