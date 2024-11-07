import time
from datetime import datetime
import datetime
import os
import dataManager
from openpyxl import Workbook
import writeToExcel

def one_minute(first_run):

    # current minute to int
    from datetime import datetime
    now = datetime.now()
    min_cur = now.minute

    # sets current min to int to be comparable
    current_min_before = int(min_cur)

    if first_run:
        pass
    else:
        time.sleep(45) # sleep 45 seconds

    waiting_var = True # variable for while loop checking time

    while waiting_var:

        # get the current minute with the datetime library
        now = datetime.now()
        min_pres = now.minute
        current_min_present = int(min_pres)
        
        if current_min_before == current_min_present:
            time.sleep(1)
        else:
            waiting_var = False # ends loop for next minute

def one_day(first_run, first_run_of_day, file_path, num_of_days):
    from datetime import datetime
    now = datetime.now()
    day_cur = now.day
    num_days_str = 'day #' + str(num_of_days)
    print(num_days_str)

    clear_file_without_logging = False
    data_already_inFile = False
    # file_path = open(f'Data\\daily_log.txt', 'r')
    file_path_excel_direc = f'Data\\excel_directory.txt'

    if os.path.getsize(file_path_excel_direc) == 0:
        from datetime import datetime
        import datetime
        print("Detected: no excel file for storing data, creating one now!")
        now = datetime.datetime.now()
        day_name_var1 = str(now.strftime('%m'))
        day_name_var2 = str(now.strftime('%d'))
        day_name_var3 = str(now.strftime('%y'))
        current_date_str = day_name_var1 + "-" + day_name_var2 + "-" + day_name_var3
        new_excel_file = f'Excel Data\\' + f"raw_data_" + current_date_str + f".xlsx"
        # Create a new workbook and select the active worksheet
        workbook = Workbook()
        # Save the workbook to a file
        workbook.save(new_excel_file)
        file_p = f"Data\\excel_directory.txt"
        direc = open(file_p, 'r+')
        direc.write(new_excel_file)

    # if first_run_of_day:
    #     first_run = True

    if os.path.getsize(file_path) != 0 and first_run == True:
        first_run = False
        data_already_inFile = True
        print("Detected: this file already has data logged on first run")

    day_prev = ""
    if first_run != True:
        FL_usage = open(file_path, 'r')
        
        day_previous = ""
        for line in FL_usage:
            cleaned_line = ",".join(part.strip() for part in line.split(","))
            day_previous = cleaned_line
            break
        if day_previous == "":
            print('failed to log day_prev')
            clear_file_without_logging = True
        else:
            day_cur = str(day_cur)
            day_prev = str(day_previous)
            if day_cur != day_prev and data_already_inFile:
                clear_file_without_logging = True
                print('-', day_cur, '-', day_prev, '-')

    if (first_run == True):
        print('Detected: run file began')
        return 0
    elif (day_cur == day_prev and first_run == False):
        print('Detected: logged day == current day, logged minutes data')
        return 1
    elif clear_file_without_logging:
        FL_usage.close()
        if file_path == f'Data\\daily_log_9hr.txt':
            dataManager.daily_log9hr_clear()
            dataManager.daily_log_9hr_ready()
        else:
            dataManager.daily_log_24hr_clear()
            dataManager.daily_log_24hr_ready()
        print("previous data recorded logged day != current day. Data",
              "cache was cleared and NOT recorded on excel")
        return 0
    else:
        if num_of_days == 10: # change val to == 20 representing if 20 logged days have passed
            FL_usage.close()
            file_p = f'Data\\excel_directory.txt'
            direc = open(file_p, 'r+')
            for line in direc:
                cleaned_line = ",".join(part.strip() for part in line.split(","))
                excel_file = cleaned_line
                break
            excel_file_str = str(excel_file)
            writeToExcel.write_data(existing_file=excel_file_str, last_log_bool=True)
            dataManager.daily_log_clear()
            dataManager.daily_log_ready()
            dataManager.daily_log_users_clear()
            dataManager.daily_log_users_ready()
            # create a new excel file
            dataManager.new_excel_file()
        else:
            FL_usage.close()
            file_p = f'Data\\excel_directory.txt'
            direc = open(file_p, 'r+')
            for line in direc:
                cleaned_line = ",".join(part.strip() for part in line.split(","))
                excel_file = cleaned_line
                break
            excel_file_str = str(excel_file)
            writeToExcel.write_data(existing_file=excel_file_str, last_log_bool = False)
            dataManager.daily_log_clear()
            dataManager.daily_log_ready()
        print('Detected: logged day != current day, previous days data was',
              'recorded on excel AND new day log started ')
        return 2

def check_weekend():
    sleep_bool = False
    now = datetime.datetime.now()
    day_name_var = now.strftime('%A')
    day_name_str = str(day_name_var)
    if day_name_str == "Saturday" or day_name_str == "Sunday":
        print("sleeping for the weekend...")
        sleep_bool = True
    else:
        sleep_bool = False

    while sleep_bool:
        time.sleep(60)
        now = datetime.datetime.now()
        day_name_var = now.strftime('%A')
        day_name_str = str(day_name_var)
        if day_name_str == "Saturday" or day_name_str == "Sunday":
            print("zzz")
            sleep_bool = True
        else:
            print('awake again!')
            sleep_bool = False
        
def check_hour():

    from datetime import datetime
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_hour_int = int(current_hour)
    current_minute_int = int(now.strftime("%M"))

    if current_hour_int == 8 and current_minute_int == 0:
        print('Detected: start of business hours...')
        return 0

    if current_hour_int > 7 and current_hour_int < 18:
        print("Detected: business hours")
        return 1
    else:
        print("Detected: non-business hours")
        return 2
    
def new_excel_sheet():
    from datetime import datetime
    now = datetime.now()
    current_day = now.strftime('%d')
    current_day_int = int(current_day)
    if current_day_int == 16:
        print("Creating new raw data set and analyzing previous data set")
    else:
        pass