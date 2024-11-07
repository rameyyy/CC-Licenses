import subprocess
import time
import datetime
import os

file_name = ""

def start():
    subprocess.run([r'Server\\Matlab Server Status1.bat'])
    direct_list = os.listdir(r'Server\\')
    for i in direct_list:
        if (i[0:14] == "license_status"):
            files_name = r"Server\\" + i
    return files_name

def timer(num_of_seconds):
    print("Sleeping for ", num_of_seconds, "second(s)")
    time.sleep(num_of_seconds)


def remove_files():
    direct_list = os.listdir(r'Server\\')
    for i in direct_list:
        if (i[0:14] == "license_status"):
            files_name = r"Server\\" + i
            os.remove(files_name)