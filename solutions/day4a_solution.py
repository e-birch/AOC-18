import datetime


def main():

    filename = open("../inputs/day4_input.txt")
    output_file = open("../inputs/day4_input_sorted.txt", "a")
    dates_list = []
    events_dict = {}

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            minute = (line.split(" ")[0] + " " + line.split(" ")[1]).strip("[").strip("]")
            event = " ".join(line.split(" ")[2:]).rstrip()

            dates_list.append(minute)
            events_dict[minute] = event

    output_list = sorted(dates_list, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M'))

    for i in output_list:
        minute_event = events_dict[i]
        write_event = i + " " + minute_event + "\n"
        output_file.write(write_event)

    output_file.close()


if __name__ == "__main__":
    main()
