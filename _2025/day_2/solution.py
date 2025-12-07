


def solve_1(solution_input):
    solution_input = solution_input[0].split(",")
    
    answer = 0
    for id_range in solution_input:
        low, high = id_range.split("-")


        if len(low) % 2 == 1:
            low = str(10 ** (len(low)))
        if int(low) > (int_high := int(high)):
            continue

        done = False
        while (int_low := int(low)) <= int_high and not done:
            current=low[:len(low) // 2]
            for i in range(int(current), 10 ** len(current)):
                current_invalid = int(str(i) + str(i))
                if current_invalid >= int_low and current_invalid <= int_high:
                    answer += current_invalid
                if current_invalid >= int_high:
                    done = True
                    break
            else:
                low = str(10 ** len(low))
                if len(low) % 2 == 1:
                    low = str(int(low) * 10)
    return answer


def solve_2(solution_input):
    solution_input = solution_input[0].split(",")
    
    answer = 0
    for id_range in solution_input:
        low, high = id_range.split("-")


        if len(low) % 2 == 1:
            low = str(10 ** (len(low)))
        if int(low) > (int_high := int(high)):
            continue

        done = False
        while (int_low := int(low)) <= int_high and not done:
            current=low[:len(low) // 2]
            for i in range(int(current), 10 ** len(current)):
                current_invalid = int(str(i) + str(i))
                if current_invalid >= int_low and current_invalid <= int_high:
                    answer += current_invalid
                if current_invalid >= int_high:
                    done = True
                    break
            else:
                low = str(10 ** len(low))
                if len(low) % 2 == 1:
                    low = str(int(low) * 10)

    return answer