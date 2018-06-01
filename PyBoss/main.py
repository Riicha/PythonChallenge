from os import path, makedirs # fetch path and makedirs function from os file
import csv
from Employee import Employee
from glob import glob # fetching glob function only from the glob lib



filePath = 'C:\\Python\\May31HomeWork\\PyBoss\\raw_data'

employee_dictionary = {} # dictionary to store the employee details
duplicateEmployees =[]
#csvpath = os.path.join('..',filePath,'employee_data1.csv')
#filesInDirectory = os.listdir(filePath) 

csvFilesOnly = glob(filePath+"\\*.csv")# parse CSV file(s) only

us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

employeeCount = 0
for csvFile in csvFilesOnly:
    firstRow = 0   
    emp_key = 1
    with open(csvFile, newline='') as csvfile: # construct to load a csv file
        csvreader = csv.reader(csvfile, delimiter=',') # object to read the file's 1 row at a time

        for row_Col in csvreader: #  Each line is read as a row here
            if (row_Col[0] !="" and firstRow !=0): # ensure the employee id is not "" & skip the first row
                employeeCount += 1   
                # In python we do need to check for dupes 
                # as dupes are automatically overriten when we assign 
                # the data set provide has 649 employess with same EmpIds
                # if (row_Col[0] in employee_dictionary):
                #     #pass
                #     # We already have this record
                #     emp = Employee(row_Col[0],row_Col[1],row_Col[2],row_Col[3],row_Col[4])
                #     duplicateEmployees.append(emp.DisplayEmployee())
                #     print( "Duplicate employee :"+emp.DisplayEmployee())
                # else:
                state = us_state_abbrev[row_Col[4]]
                # make a new employee
                emp = Employee(row_Col[0],row_Col[1],row_Col[2],row_Col[3],state)
                # add the newly created employee to the employee collection
                #employee_dictionary[emp.EmployeeId +"_"+emp.SSN +"_"+emp.FirstName+"_"+emp.LastName+"_"+emp.DOB] = emp 
                employee_dictionary[emp.DisplayEmployee()] = emp        
            
            firstRow = 1    

filePath = 'C:\\python-challenge\\PyBoss\\output'
#Check if output folder exist, create if not exists!
if not path.exists(filePath):
    makedirs(filePath)

outputFile = filePath +"\\outputEmployee.csv"
#We are opening in new file and overiting if it exist.
with open(outputFile, 'w') as csvfile:
    employeeWriter = csv.writer(csvfile)
    # Need to insert the header row with the added column
    employeeWriter.writerow("Emp ID,First Name,Last Name, DOB,SSN,State".split(","))
    for e in employee_dictionary.items():
       #print(e[1].EmployeeId + "," + e[1].FirstName +"," + e[1].LastName + "," + e[1].DOB + "," + e[1].SSN + "," + e[1].State )
       print(e[1].DisplayEmployee())
       employeeWriter.writerow(e[1].DisplayEmployee().split(","))

print("\nEmployee Count:"+str(employeeCount))

