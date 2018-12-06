
def main():
    filename = open("day1_input.txt")
    input_list = []
    count_list = [0]
    count = 0

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            input_list.append(line)

    index_count = 0

    while True:
        if index_count == len(input_list):
            index_count = 0

        sign = input_list[index_count][0]
        num = int(input_list[index_count][1:])

        index_count = index_count + 1

        if sign == "+":
            count = count + num
        else:
            count = count - num

        if count in count_list:
            print count
            break
        else:
            count_list.append(count)


if __name__ == "__main__":
    main()
