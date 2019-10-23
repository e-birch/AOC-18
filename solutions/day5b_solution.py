import operator


def main():

    filename = open("../inputs/day5_input.txt")

    full_puzzle_input = filename.read()

    polymers = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
                "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
                "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for p in polymers:
        # print p
        # print len(full_puzzle_input)
        puzzle_input = full_puzzle_input.replace(p, "").replace(p.upper(), "")
        # print len(puzzle_input)
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

        polymers[p] = len(puzzle_input)

    choice = min(polymers.iteritems(), key=operator.itemgetter(1))[0]

    # print polymers
    print choice
    print polymers[choice]







if __name__ == "__main__":
    main()