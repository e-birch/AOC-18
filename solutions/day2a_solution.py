def main():
    filename = open("day2_input.txt")
    count_dict = {2: 0, 3: 0}

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            letters_dict = {}
            for letter in line:
                if letter in letters_dict:
                    letters_dict[letter] = letters_dict[letter] + 1
                else:
                    letters_dict[letter] = 1

            for letter in letters_dict:
                if letters_dict[letter] == 2:
                    count_dict[2] = count_dict[2] + 1
                    break
            for letter in letters_dict:
                if letters_dict[letter] == 3:
                    count_dict[3] = count_dict[3] + 1
                    break

    print count_dict[2] * count_dict[3]












if __name__ == "__main__":
    main()