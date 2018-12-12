import datetime
import operator


def main():

    filename = open("../inputs/day4_input_sorted.txt")
    fmt = '%Y-%m-%d %H:%M'
    guards_dict = {}

    while True:
        line = filename.readline()
        if line == "":
            break
        else:
            line = line.split(" ")
            if line[2] == "Guard":
                curr_guard_id = int(line[3].strip("#"))
                if curr_guard_id not in guards_dict:
                    guards_dict[curr_guard_id] = {}

    filename.close()
    filename = open("../inputs/day4_input_sorted.txt")

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

                current_guard_mins_dict = guards_dict[curr_guard_id]

                for i in range(0, minutes_diff, 1):
                    curr_minute = (start_time + datetime.timedelta(minutes=i)).minute
                    if curr_minute not in current_guard_mins_dict:
                        current_guard_mins_dict[curr_minute] = 1
                    else:
                        current_guard_mins_dict[curr_minute] = current_guard_mins_dict[curr_minute] + 1
                guards_dict[curr_guard_id] = current_guard_mins_dict

    # print guards_dict

    max_guards_dict = {}

    for i in guards_dict:
        guard_nums = guards_dict[i]
        if guard_nums != {}:
            max_minute = max(guard_nums.iteritems(), key=operator.itemgetter(1))[0]
            max_guards_dict[i] = (max_minute, guard_nums[max_minute])

    print max_guards_dict
    max_guard_id = 0
    max_minute = 0
    minute_freq = 0

    for i in max_guards_dict:
        minute = max_guards_dict[i][0]
        frequency = max_guards_dict[i][1]

        if frequency > minute_freq:
            max_guard_id = i
            max_minute = minute
            minute_freq = frequency

    print max_guard_id
    print max_minute






if __name__ == "__main__":
    main()
