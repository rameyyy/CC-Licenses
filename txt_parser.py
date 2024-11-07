#comment

class mainParser:
    
    def parser(file_name):

        # Opens files
        open_file = open(file_name)
        file_obj_write = open(r"Data\\All_licenses.txt", 'w')

        # Defines function variables
        check_1 = 0
        check_2 = 0
        check_3 = 0
        check_4 = 0
        check_5 = 0
        check_6 = 0
        check_7 = 0
        check_8 = 0
        check_9 = 0
        check_10 = 0
        check_11 = 0
        check_12 = 0
        check_13 = 0
        check_14 = 0
        check_15 = 0
        check_16 = 0
        check_17 = 0
        line_num = -1

        # Parses file
        for line in open_file:
            
            # Cleans out white space
            cleaned_line = ",".join(part.strip() for part in line.split(","))

            # Increments line number
            line_num += 1

            #print(cleaned_line)

            # The next two if statements check for expected text and store which line that is in a list
            if (cleaned_line[0:15] == "Users of MATLAB" and check_1 != 1):
                check_1 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:17] == "Users of SIMULINK" and check_2 != 1):
                check_2 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:24] == "Users of Control_Toolbox" and check_3 != 1):
                check_3 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:27] == "Users of RTW_Embedded_Coder" and check_4 != 1):
                check_4 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:21] == "Users of MATLAB_Coder" and check_5 != 1):
                check_5 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")
            
            if (cleaned_line[0:26] == "Users of MATLAB_Report_Gen" and check_6 != 1):
                check_6 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:30] == "Users of Simulink_Requirements" and check_7 != 1):
                check_7 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:21] == "Users of SimDriveline" and check_8 != 1):
                check_8 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")
            
            if (cleaned_line[0:17] == "Users of Simscape" and check_9 != 1):
                check_9 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")
                
            if (cleaned_line[0:27] == "Users of Real-Time_Workshop" and check_10 != 1):
                check_10 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")
            
            if (cleaned_line[0:26] == "Users of Simulink_Coverage" and check_11 != 1):
                check_11 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:28] == "Users of SIMULINK_Report_Gen" and check_12 != 1):
                check_12 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:22] == "Users of Simulink_Test" and check_13 != 1):
                check_13 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:18] == "Users of Stateflow" and check_14 != 1):
                check_14 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:32] == "Users of Vehicle_Network_Toolbox" and check_15 != 1):
                check_15 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:23] == "Users of Signal_Toolbox" and check_16 != 1):
                check_16 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

            if (cleaned_line[0:27] == "Users of Statistics_Toolbox" and check_17 != 1):
                check_17 = 1
                data = cleaned_line
                file_obj_write.write(data)
                file_obj_write.write("\n")

