import startServer
from floating_ML_finder import floating_ML_parser
from txt_parser import mainParser
import dataManager
import dailyLog
import TimeKeeper
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk


# root = Tk()
# root.geometry("400x300")
# root.title("File Manager V1.0 --> NOT RUNNING")

# program_running = False

# def start_log():
#     program_running = True
#     root.title("File Manager V1.0 --> STARTING")
#     time.sleep(3)
#     root.destroy()


# button1 = tk.Button(root,
#                    text="Start Log",
#                    command=start_log,
#                    activebackground="blue", 
#                    activeforeground="white",
#                    anchor="center",
#                    bd=3,
#                    bg="white",
#                    cursor="hand2",
#                    disabledforeground="gray",
#                    fg="black",
#                    font=("Arial", 12),
#                    height=2,
#                    highlightbackground="black",
#                    highlightcolor="green",
#                    highlightthickness=2,
#                    justify="center",
#                    overrelief="raised",
#                    padx=5,
#                    pady=1,
#                    width=15,
#                    wraplength=100)
# button1.pack(padx=20, pady=20)

# text_box = Text(height=4, width=45)
# text_box.pack(expand=True)
# text_box.insert('end', f'README: Once you press start, this window\nwill close in 3 seconds, and the logger will\nstart!')
# text_box.config(state='disabled')

# root.mainloop()

num_of_days = 1
first_run = True
day_logged = 0
exceptions_valid = True
first_run_of_day = False
first_run_of_day9hr = False

while exceptions_valid == True:
    try:
        #checks for business hours
        # TimeKeeper.check_hour()

        #runs the server and creates new server data file
        file_name = startServer.start()

        # check floating ML licenses & store in data txt file
        range = floating_ML_parser.find_FloatingLicenses(file_name)
        floating_ML_parser.write_FL_txt(file_name, range)

        #retrieve all other license information and store in second data file
        mainParser.parser(file_name)

        #stores information from two data files into daily logger counting txt file
        run_both_loggers = TimeKeeper.check_hour()
        if run_both_loggers == 1:
            file_path24 = f'Data\\daily_log.txt'
            file_path9 = f'Data\\daily_log_9hr.txt'
            DL_use_time = TimeKeeper.one_day(first_run, first_run_of_day, file_path24, num_of_days)
            if DL_use_time == 2:
                first_run_of_day = True
                num_of_days +=1
            else:
                first_run_of_day = False
            dailyLog.daily_logger(DL_use_time, file_path24)
            DL_use_time = TimeKeeper.one_day(first_run, first_run_of_day, file_path9, num_of_days)
            if DL_use_time == 2:
                first_run_of_day = True
                num_of_days +=1
            else:
                first_run_of_day = False
            dailyLog.daily_logger(DL_use_time, file_path9)
        elif run_both_loggers == 2:
            file_path24 = f'Data\\daily_log.txt'
            DL_use_time = TimeKeeper.one_day(first_run, first_run_of_day, file_path24, num_of_days)
            if DL_use_time == 2:
                first_run_of_day = True
                if num_of_days == 10: #if its been 10 business days
                    num_of_days = 1 #back to day 1
                else:
                    num_of_days +=1
            else:
                first_run_of_day = False
            dailyLog.daily_logger(DL_use_time, file_path24)
        elif run_both_loggers == 0:
            print("new day for 9hr data log...")
            file_path24 = f'Data\\daily_log.txt'
            file_path9 = f'Data\\daily_log_9hr.txt'
            dailyLog.daily_logger(1, file_path24)
            dataManager.daily_log9hr_clear()
            dataManager.daily_log_9hr_ready()
            dailyLog.daily_logger(0, file_path9)


        #data file management, clears data for next use after data goes to excel
        dataManager.empty_data()
        dataManager.ready_file()

        #deletes server raw data txt file after parsing
        startServer.remove_files()

        #sleeps for 1 minute before running again
        TimeKeeper.one_minute(first_run)
        first_run = False
        TimeKeeper.check_weekend()

    except Exception as failed_run:
        print(failed_run)
        check_hr = TimeKeeper.check_hour()
        if check_hr == True:
            exceptions_valid = dailyLog.exception_counter(f'Data\\daily_log_9hr.txt')
            exceptions_valid = dailyLog.exception_counter(f'Data\\daily_log.txt')
            print('failed run, retrying in one minute...')
        else:
            exceptions_valid = dailyLog.exception_counter(f'Data\\daily_log.txt')
            print('failed run, retrying in one minute...')
        time.sleep(60)



