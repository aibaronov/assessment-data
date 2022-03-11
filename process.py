#Opens the 'um-server-01.txt' file and saves it to a variable called 'log-file'
log_file = open("um-server-01.txt")

#creates a function called sales report.
#This function access the content of the text file

# def sales_reports(log_file):
#     #this loops through each line of the file using the variable 'line'
#     for line in log_file:
#         #strips any trailing character from the end of the string
#         line = line.rstrip()
#         #The first three characters of each line are the day of the week
#         #The variable day access those characters
#         day = line[0:3]
#         #Prints the line where the day of the week is Tuesday
#         if day == "Tue":
#             print(line)

def sales_reports(log_file):
    #this loops through each line of the file using the variable 'line'
    for line in log_file:
        #strips any trailing character from the end of the string
        line = line.rstrip()
        #The first three characters of each line are the day of the week
        #The variable day access those characters
        day = line[0:3]
        #Prints the line where the day of the week is Tuesday
        if day == "Mon":
            print(line)



sales_reports(log_file)
