#Opens the 'um-server-01.txt' file and saves it to a variable called 'log-file'
log_file = open("um-server-01.txt")

#creates a function called sales report.
#This function access the content of the text file

def sales_reports(log_file):
    #this loops through each line of the file using the variable 'line'
    for line in log_file:
        #strips any white space from each line
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)
