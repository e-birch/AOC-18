
def get_letters_dict(line_list):
    letters_dict = {}

    for i in line_list:

        if i[0] not in letters_dict:
            letters_dict[i[0]] = [i[1]]
        else:
            letters_dict[i[0]].append(i[1])

    return letters_dict


def read_file_into_list(input_filename):
    filename = open(input_filename)
    relations_list = []

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            line_list = line.strip("\n").split(" ")
            relations_list.append((line_list[1], line_list[7]))
    return relations_list

def main():

    input_filename = "../inputs/day7_input_test.txt"

    line_list = read_file_into_list(input_filename)
    letters_dict = get_letters_dict(line_list)

    unblocked_letters = set()

    for i in letters_dict:
        unblocked_letters.add(i)
        for j in letters_dict[i]:
            unblocked_letters.add(j)

    for i in letters_dict:
        blocked_letters = letters_dict[i]
        for j in blocked_letters:
            if j in unblocked_letters:
                unblocked_letters.remove(j)

    print unblocked_letters
    print letters_dict




if __name__ == "__main__":
    main()
