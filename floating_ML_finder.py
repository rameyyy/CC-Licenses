#comment
class floating_ML_parser():


    def test_run(file_name):
        open_file = open(file_name)
        line_num = -1
        for line in open_file:
            cleaned_line = ",".join(part.strip() for part in line.split(","))
            line_num += 1
            print(line_num, cleaned_line)

    def find_FloatingLicenses(file_name):

        # Opens file
        open_file = open(file_name)

        # Defines function variables
        i = 0
        j = 0
        check_1 = 0
        line_num_total = -1
        line_range = []
        # Parses file
        for line in open_file:

            # Cleans out white space
            cleaned_line = ",".join(part.strip() for part in line.split(","))
            
            # Increments line number
            line_num_total += 1

            # The next two if statements check for expected text and store which line that is in a list
            if (cleaned_line == "floating license" and j != 1):
                j = 1
                line_range.append(line_num_total+2)

            if (cleaned_line[0:17] == "Users of SIMULINK" and j==1):
                line_range.append(line_num_total-2)
                break

            # Gets time stamp
            if (cleaned_line[0:31] == "Flexible License Manager status" and check_1 !=1):
                check_1 = 1
                file_obj_write_1 = open(r"Data\\Time_stamp.txt", 'w')
                data = cleaned_line[35:58]
                file_obj_write_1.write(data)

        return line_range

    def write_FL_txt(file_to_read, line_range):
        file_obj_write = open(r"Data\\FLWrite.txt", 'w')
        check_line_range = len(line_range)
        if check_line_range == 2:
            range_1 = line_range[0]
            range_2 = line_range[1]+1
            num_of_users = range_2-range_1
            for i in range(range_1,range_2):
                with open(file_to_read) as f:
                    FL_ML_data = f.readlines()[i]
                    file_obj_write.write(FL_ML_data)
            file_obj_write.write("Total number of current people using the floating matlabl license: ")
            file_obj_write.write(str(num_of_users))
            file_obj_write.write(f'/2')
        else:
            file_obj_write.write("0 current FL ML licenses being used")
        file_obj_write.close()