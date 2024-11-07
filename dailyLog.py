#comment
#import pandas as pd
from openpyxl import load_workbook
import os
from datetime import datetime
import dataManager
import writeToExcel

#Global data variables

def replace_line(file_path, line_number, new_line_content):
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Replace the specific line
    if 0 <= line_number < len(lines):
        lines[line_number] = new_line_content + '\n'  # Add newline character if needed
    else:
        raise IndexError("Line number is out of range")
    
    # Step 3: Write the file with the updated content
    with open(file_path, 'w') as file:
        file.writelines(lines)


def decode_username(username):

    real_name = "not-found"
    # open txt file with username info
    decoder_file = open(f'Data\\username_decoder.txt')

    found_match = False

    for line in decoder_file:

        # cleans lines just in case
        cleaned_line = ",".join(part.strip() for part in line.split(","))

        if found_match:
            real_name = str(cleaned_line[7:50])
            break

        user_code = str(cleaned_line[9:15])
        if user_code == username:
            found_match = True

    if found_match:
        return real_name
    else:
        return username

def exception_counter(file_path):
    # track users daily usage %
    FL_usage = open(file_path, 'r+')

    for line in FL_usage:
        if line[0:10] == "exceptions":
            if line[13:14] == " ":
                new_num = int(line[12:13])
                new_num += 1
                new_num_str = str(new_num)
                replace_str = "exceptions: " + new_num_str + " "
                print(replace_str)
                replace_line(file_path, 1, replace_str)
                return True
            elif line[14:15] == " ":
                new_num = int(line[12:14])
                new_num += 1
                new_num_str = str(new_num)
                replace_str = "exceptions: " + new_num_str + " "
                print(replace_str)
                replace_line(file_path, 1, replace_str)
                return True
            elif line[15:16] == " ":
                new_num = int(line[12:15])
                new_num += 1
                new_num_str = str(new_num)
                replace_str = "exceptions: " + new_num_str + " "
                print(replace_str)
                replace_line(file_path, 1, replace_str)  
                return True   
            elif line[16:17] == " ":
                print('Program failure, exceptions > 999')
                FL_usage.close()
                return False
    FL_usage.close()

def daily_logger(DL_use_time_info, file_path):

    FL_usage = open(file_path, 'r+')

    FL_ML_file = open(f'Data\\FLWrite.txt')
    time_stamp_file = open(f'Data\\Time_stamp.txt')
    all_licenses_file = open(f'Data\\All_licenses.txt')

    # function variables
    line_num = -1
    current_users_data = 0 # holds value for how many current FL users
    start_time_u1 = None # holds value for start time of user1
    start_time_u2 = None # holds value for start time of user2
    user_1 = ""
    user_2 = ""
    current_time = ""

    # loops data from FLWrite.txt file
    for line in FL_ML_file:
            
        # Cleans out white space
        cleaned_line = ",".join(part.strip() for part in line.split(","))

        # Increments line number
        line_num += 1
        if (cleaned_line[0:36] == "Total number of current people using"):
            num_of_users = cleaned_line[-3]
            current_users_data = int(num_of_users)
        elif (cleaned_line[0:26] == "0 current FL ML licenses b"):
            current_users_data = 0
            break   
        else:
            if user_1 == "":
                str1 = str(cleaned_line[-9:-1])
                str2 = str(cleaned_line[-1])
                start_time_u1 = (str1 + str2)
                user_1_x = str(cleaned_line[0:6])
                user_1 = decode_username(user_1_x)
            else:
                str1 = str(cleaned_line[-9:-1])
                str2 = str(cleaned_line[-1])
                start_time_u2 = (str1 + str2)
                user_2_x = str(cleaned_line[0:6])
                user_2 = decode_username(user_2_x)
                

    # gets current time from time_stamp.txt file    
    for line in time_stamp_file:
        
        # Cleans out white space
        cleaned_line = ",".join(part.strip() for part in line.split(","))

        str1 = str(cleaned_line[-16:-1])
        str2 = str(cleaned_line[-1])
        current_time = str1 + str2

    specific_new_data = []
    new_data = []
    # gets all licenses usage data from All_licenses.txt file
    for line in all_licenses_file:

        # Cleans out white space
        cleaned_line = ",".join(part.strip() for part in line.split(","))

        # variable initialization
        license_plural = str(cleaned_line[-9])
        licenses_used = 999
        licenses_total = 999

        # if first license in text file HAS an 's'
        if license_plural == 's':

            # if licenses used number is one digit
            if (str(cleaned_line[-19]) == ' '):
                licenses_used = int(cleaned_line[-18])

                # if second license in text file HAS an 's'
                if (str(cleaned_line[-38]) == 's'):
                    licenses_total = int(cleaned_line[-48:-46])

                # if second license in text file DOES NOT have an 's'
                else:
                    licenses_total = int(cleaned_line[-47:-45])
            
            # if licenses used number is two digits
            else:
                licenses_used = int(cleaned_line[-19:-17])

                # if second license in text file HAS an 's'
                if (str(cleaned_line[-39]) == 's'):
                    licenses_total = int(cleaned_line[-49:-47])
                
                # if second license in text file DOES NOT have an 's'
                else:
                    licenses_total = int(cleaned_line[-48:-46])

        # if first license in text file DOES NOT have an 's'
        else:

            # if licenses used number is one digit
            if (str(cleaned_line[-18]) == ' '):
                licenses_used = int(cleaned_line[-17])

                # if second license in text file HAS an 's'
                if (str(cleaned_line[-37]) == 's'):
                    licenses_total = int(cleaned_line[-47:-45])

                # if second license in text file DOES NOT have an 's'
                else:
                    licenses_total = int(cleaned_line[-46:-44])

            # # if licenses used number is NOT one digit
            else:
                licenses_used = int(cleaned_line[-18:-16])

                # if second license in text file HAS an 's'
                if (str(cleaned_line[-38]) == 's'):
                    licenses_total = int(cleaned_line[-48:-46])
                
                # if second license in text file DOES NOT have an 's'
                else:
                    licenses_total = int(cleaned_line[-47:-45])
            
        # New data to append
        new_data.append(licenses_used)
        specific_new_data.append(licenses_used)
        new_data.append(licenses_total)

    # this is the first run
    if DL_use_time_info == 0:
        now = datetime.now()
        day_cur = now.day
        day_logged = str(day_cur)
        FL_usage.write(day_logged)
        FL_usage.write('\n')
        FL_usage.write("exceptions: 0 ")
        FL_usage.write('\n')
        if current_users_data == 0:
            FL_usage.write('0 user: 1 ')
            FL_usage.write('\n')
        else:
            FL_usage.write('0 user: 0 ')
            FL_usage.write('\n')
        if current_users_data == 1:
            FL_usage.write('1 user: 1 ')
            FL_usage.write('\n')
        else:
            FL_usage.write('1 user: 0 ')
            FL_usage.write('\n')
        if current_users_data == 2:
            FL_usage.write('2 user: 1 ')
            FL_usage.write('\n')
        else:
            FL_usage.write('2 user: 0 ')
            FL_usage.write('\n')
        for data in new_data:
            data_str = str(data)
            FL_usage.write(data_str)
            FL_usage.write(' \n')
        if (user_1 != "" and user_2 != ""):
            FL_usage.write(user_1)
            FL_usage.write(' 1 ')
            FL_usage.write('\n')
            FL_usage.write(user_2)
            FL_usage.write(' 1 ')
            FL_usage.write('\n')
            two_users = True
        elif (user_1 != "" and user_2 == ""):
            FL_usage.write(user_1)
            FL_usage.write(" 1 ")
            FL_usage.write('\n')
            one_users = True
        else:
            pass

                    
            


    loop_count = 0
    user_1_already_exists = False
    user_2_already_exists = False
    FL_usage.close()
    FL_usage = open(file_path, 'r+')
    # day has not changed & it is not the first run
    if DL_use_time_info == 1:
        for line in FL_usage:
            # clean line
            cleaned_line = ",".join(part.strip() for part in line.split(","))
            if loop_count > 38:
                if user_1_already_exists != True:
                    if cleaned_line[0:6] == user_1[0:6]:
                        users_len = len(user_1)
                        users_len = int(users_len)
                        users_len +=1
                        new_val_ = cleaned_line[users_len:99]
                        new_val_int = int(new_val_)
                        new_val_int += 1
                        new_val_str = str(new_val_int)
                        replace_str = user_1 + " " + new_val_str + " "
                        replace_line(file_path, loop_count, replace_str)
                        user_1_already_exists = True
                if user_2_already_exists != True:
                    if cleaned_line[0:6] == user_2[0:6]:
                        users_len = len(user_2)
                        users_len = int(users_len)
                        users_len +=1
                        new_val_ = cleaned_line[users_len:99]
                        new_val_int = int(new_val_)
                        new_val_int += 1
                        new_val_str = str(new_val_int)
                        replace_str = user_2 + " " + new_val_str + " "
                        replace_line(file_path, loop_count, replace_str)
                        user_2_already_exists = True
            loop_count += 1

        if user_1_already_exists != True and user_1 != "":
                FL_usage.write(user_1)
                FL_usage.write(' 1')
                FL_usage.write(' \n')

        if user_2_already_exists != True and user_2 != "":
                FL_usage.write(user_2)
                FL_usage.write(' 1')
                FL_usage.write(' \n')
        
        # num of users data
        FL_usage.close()
        FL_usage = open(file_path, 'r+')
        num_of_users = current_users_data
        for line in FL_usage:
            if num_of_users == 0:
                if line[0:6] == '0 user':
                    if line[9] == " ":
                        users_num = int(line[8])
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "0 user: " + users_num + " "
                        replace_line(file_path, 2, new_str)
                    elif line[10] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num = users_num1 + users_num2
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "0 user: " + users_num + " "
                        replace_line(file_path, 2, new_str)
                    elif line[11] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num3 = str(line[10])
                        users_num = users_num1 + users_num2 + users_num3
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "0 user: " + users_num + " "
                        replace_line(file_path, 2, new_str)
                    elif line[12] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num3 = str(line[10])
                        users_num4 = str(line[11])
                        users_num = users_num1 + users_num2 + users_num3 + users_num4
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "0 user: " + users_num + " "
                        replace_line(file_path, 2, new_str)
            elif num_of_users == 1:
                if line[0:6] == '1 user':
                    if line[9] == " ":
                        users_num = int(line[8])
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "1 user: " + users_num + " "
                        replace_line(file_path, 3, new_str)
                    elif line[10] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num = users_num1 + users_num2
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "1 user: " + users_num + " "
                        replace_line(file_path, 3, new_str)
                    elif line[11] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num3 = str(line[10])
                        users_num = users_num1 + users_num2 + users_num3
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "1 user: " + users_num + " "
                        replace_line(file_path, 3, new_str)
                    elif line[12] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num3 = str(line[10])
                        users_num4 = str(line[11])
                        users_num = users_num1 + users_num2 + users_num3 + users_num4
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "1 user: " + users_num + " "
                        replace_line(file_path, 3, new_str)
            elif num_of_users == 2:
                if line[0:6] == '2 user':
                    if line[9] == " ":
                        users_num = int(line[8])
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "2 user: " + users_num + " "
                        replace_line(file_path, 4, new_str)
                    elif line[10] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num = users_num1 + users_num2
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "2 user: " + users_num + " "
                        replace_line(file_path, 4, new_str)
                    elif line[11] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num3 = str(line[10])
                        users_num = users_num1 + users_num2 + users_num3
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "2 user: " + users_num + " "
                        replace_line(file_path, 4, new_str)
                    elif line[12] == " ":
                        users_num1 = str(line[8])
                        users_num2 = str(line[9])
                        users_num3 = str(line[10])
                        users_num4 = str(line[11])
                        users_num = users_num1 + users_num2 + users_num3 + users_num4
                        users_num = int(users_num)
                        users_num += 1
                        users_num = str(users_num)
                        new_str = "2 user: " + users_num + " "
                        replace_line(file_path, 4, new_str)
        
        # all license usage % functionality
        line_counter = 0
        index_counter = 0
        FL_usage.close()
        FL_usage = open(file_path, 'r+')
        for line in FL_usage:
            if (line_counter > 4) and (line_counter % 2 == 1):
                if line_counter > 37:
                    break
                else:
                    if line[1] == " ":
                        old_num_var = str(line[0])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)                    
                    elif line[2] == " ":
                        old_num_var = str(line[0:2])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[3] == " ":
                        old_num_var = str(line[0:3])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[4] == " ":
                        old_num_var = str(line[0:4])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[5] == " ":
                        old_num_var = str(line[0:5])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[6] == " ":
                        old_num_var = str(line[0:6])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[7] == " ":
                        old_num_var = str(line[0:7])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[8] == " ":
                        old_num_var = str(line[0:8])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    elif line[9] == " ":
                        old_num_var = str(line[0:9])
                        old_num = float(old_num_var)
                        new_num_var = specific_new_data[index_counter]
                        new_num = float(new_num_var)
                        new_usage_var = (old_num + new_num)
                        new_usage = "{:.1f}".format(new_usage_var)
                        new_usage_str = str(new_usage)
                        new_usage_str = new_usage_str + " "
                        replace_line(file_path, line_counter, new_usage_str)
                    else:
                        pass
                    
                    index_counter += 1
            line_counter += 1





    # if its a new day, write data from daily log to excel and clear the daily log
    # this has no logic, this is done in the writeToExcel.py file, pushed from the driver
    if DL_use_time_info == 2:
        pass
    
    FL_usage.close()

    # run status message:
    print("Successfully ran at: ", current_time)