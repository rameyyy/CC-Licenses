import os
from openpyxl import Workbook
import datetime

def empty_data():
    os.remove(r'Data\\All_licenses.txt')
    os.remove(r'Data\\FLWrite.txt')
    os.remove(r'Data\\Time_stamp.txt')

def ready_file():
    with open(f"Data\\All_licenses.txt", 'w') as file_1:
        pass
    with open(f"Data\\FLWrite.txt", 'w') as file_2:
        pass
    with open(f"Data\\Time_stamp.txt", 'w') as file_3:
        pass

def daily_log9hr_clear():
    os.remove(r'Data\\daily_log_9hr.txt')

def daily_log_9hr_ready():
    with open(f"Data\\daily_log_9hr.txt", 'w') as file_5:
        pass

def daily_log_24hr_clear():
    os.remove(r'Data\\daily_log.txt')

def daily_log_24hr_ready():
    with open(f"Data\\daily_log.txt", 'w') as file_5:
        pass

def daily_log_users_clear():
    os.remove(r'Data\\daily_log_users.txt')

def daily_log_users_ready():
    with open(f"Data\\daily_log_users.txt", 'w') as file_5:
        pass

def daily_log_clear():
    os.remove(r'Data\\daily_log.txt')
    os.remove(r'Data\\daily_log_9hr.txt')

def daily_log_ready():
    with open(f"Data\\daily_log.txt", 'w') as file_4:
        pass
    with open(f"Data\\daily_log_9hr.txt", 'w') as file_5:
        pass

def excel_direc_clear():
    os.remove(r'Data\\excel_directory.txt')

def excel_direc_ready():
    with open(f"Data\\excel_directory.txt", 'w') as file_6:
        pass

def new_excel_file():
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
    print(new_excel_file, "created for the week!")
    direc = open(file_p, 'r+')
    direc.write(new_excel_file)