from os import path, makedirs # fetch path and makedirs function from os file
import csv # fetch csv file
from glob import glob # fetching glob function only from the glob lib

output
filePath = 'C:\\python-challenge\\PyBank\\raw_data'
csvFilesOnly = glob(filePath + "\\*.csv") # path to pickup all .csv files


total_number_of_months = 0
total_revenue = 0.00
collection = [] # List to store all the revenues
month_rev_dictionary = {} # dictionary to store the months and their revenue


for csvFile in csvFilesOnly:

    with open(csvFile, newline='') as csvDataFile: # construct to load a csv file
        csvreader = csv.reader(csvDataFile, delimiter=',') # object to read the file's 1 row at a time

        firstRow = True
        for row in csvreader: #  Each line is read as a row here
       
            if (row[1] !="" and firstRow == False): # ensure the revenue is not "" & skip the first row
                total_number_of_months +=1  # calculate total number of months
                total_revenue += float(row[1].strip())  # calculate total revenue
                collection.append(float(row[1].strip())) # populate the list / collection
                month_rev_dictionary[row[0]] = float(row[1]) # populate the dictionary with keys and their respective values
       
            firstRow = False # boolean to make the control go to next row in second iteration

    
previous_rev = 0.0
deltaComputed = 0.0
delta_rev = []

  
greatest_rev = 0
least_rev = 0
for rev in collection:
    delta_rev.append(rev - previous_rev)
    if (greatest_rev < rev ): # condition to check for greater revenue and assign it to greatest_rev
        greatest_rev = rev
    if (least_rev > rev): # condition to check for least revenue and assign it to least revenue_rev & prev revevenue
        least_rev = rev
    previous_rev = rev


delta_summation = 0.0
for d in delta_rev:
    delta_summation += d

search_max_month = ""
search_min_month = ""

for month in month_rev_dictionary.keys():
    if (greatest_rev ==  month_rev_dictionary[month]) :# check greater revenue
        search_max_month = month
    if (least_rev == month_rev_dictionary[month]):# check least revenue
        search_min_month = month
    if (search_max_month != "" and search_min_month != "" ):# break when the rows are empty.
        break

# write in the output file

filePath = 'C:\\python-challenge\\PyBank\\output'
#Check if output folder exist, create if not exists!
if not path.exists(filePath):
    makedirs(filePath)

outputFile = filePath +"\\outputBank.txt"
# Opening in new file and overiting if it exist.
f = open(outputFile,'w')
f.write("**************************************************************************************************************************************************")
f.write("\n")
f.write("Financial Analysis")
f.write("\n\nTotal Months: " + str(total_number_of_months) + " months")
f.write("\n\nTotal Revenue:  $ " + str(total_revenue) )
f.write("\n\nAverage Revenue Change: " + str(delta_summation/total_number_of_months) )
f.write("\n\nGreatest Increase in Revenue: "  + search_max_month + '  (${:,}'.format(greatest_rev)+ ")" ) 
f.write("\n\nGreatest Decrease in Revenue: "+ search_min_month + '  (${:,}'.format(least_rev) + ")" )
f.write("\n")
f.write("\n\n**************************************************************************************************************************************************")
f.close()
##################################################################################
print("\n*********************************************************************************************")
print("Financial Analysis")
print("\nTotal Months: " + str(total_number_of_months) + " months")
print("\nTotal Revenue:  $ " + str(total_revenue) )
print("\nAverage Revenue Change: " + str(delta_summation/total_number_of_months) )
print("\nGreatest Increase in Revenue: "  + search_max_month + '  (${:,}'.format(greatest_rev)+ ")" ) 
print("\nGreatest Decrease in Revenue: "+ search_min_month + '  (${:,}'.format(least_rev) + ")" )
print("\n*********************************************************************************************")



    
