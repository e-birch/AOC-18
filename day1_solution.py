
def main():
    filename = open("day1_input.txt")
    count = 0
    freq_list = []

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            if line[0] == "+":
                floor_num = int(line[1:])
                count = count + floor_num
            else:
                floor_num = int(line[1:])
                count = count - floor_num
        if count in freq_list:
            print count
            break
        else:
            freq_list.append(count)


if __name__ == "__main__":
    main()
