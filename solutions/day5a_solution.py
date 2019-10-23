def main():

    filename = open("../inputs/day5_input.txt")

    puzzle_input = filename.read()

    change_flag = 1

    while True:
        i = 0
        if change_flag == 0:
            break
        else:
            change_flag = 0

        while i < len(puzzle_input) - 1:
            character_pair = puzzle_input[i:i+2]

            if character_pair[0] != character_pair[1] and character_pair[0].upper() == character_pair[1].upper():
                puzzle_input = puzzle_input[:i] + puzzle_input[i+2:]
                change_flag = 1

            i = i + 1

    # print puzzle_input
    print len(puzzle_input)












if __name__ == "__main__":
    main()