def main():
    filename = open("day2_input.txt")
    IDs_list = []

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            IDs_list.append(line.strip('\n'))

    while True:
        if len(IDs_list) == 0:
            break
        check_word = IDs_list[0]
        IDs_list = IDs_list[1:]

        i = 0

        while i < len(check_word):
            sliced_word = check_word[:i] + check_word[i+1:]

            for word in IDs_list:
                word = word[:i] + word[i+1:]
                if sliced_word == word:
                    print sliced_word
                    break
            i = i + 1


if __name__ == "__main__":
    main()
