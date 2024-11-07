import dataManager
from openpyxl import load_workbook
import os

def rewrite_user_log(monthly_user_log):
    daily_log_users_file = open(f'Data\\daily_log_users.txt', 'r+')
    for i in monthly_user_log:
        daily_log_users_file.write(i)
        daily_log_users_file.write('\n')
    daily_log_users_file.close()

    

def get_data_and_write(existing_file, file_path, file_path_users_fn, last_log_bool):

    # initialize vars
    write_data = [[]]
    username_data = []
    line_counter = 0
    num_ = 0

    file_path_open = open(file_path, 'r+')

    for line in file_path_open:

        # clean lines spacing
        cleaned_line = ",".join(part.strip() for part in line.split(","))

        if line_counter == 1:
            write_data[0].append(int(cleaned_line[12:20]))

        if line_counter > 1 and line_counter < 5:
            write_data[0].append(int(cleaned_line[8:20]))
            num_ += int(cleaned_line[8:20])
            if line_counter == 4:
                write_data[0].append(num_)

        if line_counter > 4 and line_counter < 39:
            if line_counter%2 == 0:
                write_data[0].append(int(cleaned_line))
            else:
                float_data_raw = float(cleaned_line) / float(num_)
                float_data_formatted = float("{:.2f}".format(float_data_raw))
                write_data[0].append(float_data_formatted)

        if line_counter > 38:
            username_len = len(cleaned_line)
            len_1 = username_len - 2
            len_2 = username_len - 3
            len_3 = username_len - 4
            len_4 = username_len - 5
            if cleaned_line[len_1] == " ":
                username_data.append(str(cleaned_line[0:len_1]))
                username_data.append(int(cleaned_line[len_1+1]))
            elif cleaned_line[len_2] == " ":
                username_data.append(str(cleaned_line[0:len_2]))
                username_data.append(int(cleaned_line[len_2+1:99]))
            elif cleaned_line[len_3] == " ":
                username_data.append(str(cleaned_line[0:len_3]))
                username_data.append(int(cleaned_line[len_3+1:99]))
            elif cleaned_line[len_4] == " ":
                username_data.append(str(cleaned_line[0:len_4]))
                username_data.append(int(cleaned_line[len_4+1:99]))
        line_counter += 1
    
    file_path_open.close()
    if file_path_users_fn != "":
        monthly_user_log_data = []
        if os.path.getsize(file_path_users_fn) == 0:
            file_path_users1 = open(file_path_users_fn, 'r+')
            for data_uName in username_data:
                data_str = str(data_uName)
                file_path_users1.write(data_str)
                file_path_users1.write('\n')
            file_path_users1.close()
        else:
            file_path_users2 = open(file_path_users_fn, 'r+')
            for line in file_path_users2:
                cleaned_line = ",".join(part.strip() for part in line.split(","))
                monthly_user_log_data.append(cleaned_line)
            loop1 = 0
            data2r_num = 0
            len_of_monthly_user = int(len(monthly_user_log_data))
            for data1 in username_data:
                loop2 = 0
                for data2 in monthly_user_log_data:
                    if data1 == data2 and type(data1) == str:
                        data2r_num = int(username_data[loop1+1])
                        num1 = int(monthly_user_log_data[loop2+1])
                        new_num = data2r_num + num1
                        new_num_str = str(new_num)
                        monthly_user_log_data[loop2+1] = new_num_str
                        break
                    elif loop2+1 == len_of_monthly_user:
                        try:
                            toInt = int(data1)
                        except Exception as e:
                            monthly_user_log_data.append(data1)
                            data_str = str(username_data[loop1+1])
                            monthly_user_log_data.append("0")
                    loop2+=1
                loop1+=1
            file_path_users2.close()
            rewrite_user_log(monthly_user_log_data)

    # Load existing workbook
    wb = load_workbook(existing_file)
 
    # Select the active sheet
    ws = wb.active
 
    # Append new data
    for row in write_data:
        ws.append(row)
    
    if last_log_bool:
        user_data = [[]]
        open_fUsers = open(f'Data\\daily_log_users.txt', 'r+')
        loop_cnt = 0
        for line in open_fUsers:
            cleaned_line = ",".join(part.strip() for part in line.split(","))
            if loop_cnt % 2 == 0:
                user_data[0].append(str(cleaned_line))
            else:
                user_data[0].append(int(cleaned_line))
            loop_cnt += 1
        
        open_fUsers.close()
        
        for row in user_data:
            print(row)
            ws.append(row)
            

    # Save the workbook
    wb.save(existing_file)

def write_data(existing_file=str, last_log_bool=bool):

    # open daily logger txt file
    file_path_24hr = f'Data\\daily_log.txt'
    file_path_9hr = f'Data\\daily_log_9hr.txt'
    file_path_users = f'Data\\daily_log_users.txt'
    if last_log_bool:
        get_data_and_write(existing_file, file_path_9hr, "", False)
        get_data_and_write(existing_file, file_path_24hr, file_path_users, True)
    else:
        get_data_and_write(existing_file, file_path_24hr, file_path_users, False)
        get_data_and_write(existing_file, file_path_9hr, "", False)