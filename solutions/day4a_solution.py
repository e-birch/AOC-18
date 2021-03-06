import datetime
import operator


def main():

    filename = open("../inputs/day4_input_sorted.txt")
    fmt = '%Y-%m-%d %H:%M'
    minutes_dict = {}

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            line = line.split(" ")
            if line[2] == "Guard":
                curr_guard_id = int(line[3].strip("#"))

            elif line[2] == "falls":
                start_time = datetime.datetime.strptime(line[0] + " " + line[1], fmt)
            else:
                end_time = datetime.datetime.strptime(line[0] + " " + line[1], fmt)
                minutes_diff = (end_time - start_time).seconds / 60

                if curr_guard_id == 2851:
                    for i in range(0, minutes_diff, 1):
                        curr_minute = (start_time + datetime.timedelta(minutes=i)).minute
                        if curr_minute not in minutes_dict:
                            minutes_dict[curr_minute] = 1
                        else:
                            minutes_dict[curr_minute] = minutes_dict[curr_minute] + 1

    print minutes_dict
    max_minute = max(minutes_dict.iteritems(), key=operator.itemgetter(1))[0]
    print max_minute


if __name__ == "__main__":
    main()
