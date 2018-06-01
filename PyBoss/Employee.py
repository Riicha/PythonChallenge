from datetime import datetime
class Employee:
    """Construct employee class and its members/operations"""
    # constructor of employee class
    def __init__(self,EmployeeId,Name,DOB,SSN,State):
        """Initialize the employee and return a new employee object. """
        self.EmployeeId = EmployeeId
        # Need to split the name into First Name and Last Name
        name = Name.split(" ")
        self.FirstName = name[0]
        self.LastName = name[1]
        self.DOB = DOB
        self.SSN = SSN
        self.State = State

    # function to display employee details
    def DisplayEmployee(self):
        """ 1. It formats the DOB
            2. Masks the SSN
            3. Sends all the attributes as CSV
        """

        #Need to change the date format
        formatDate = datetime.strptime(self.DOB,'%Y-%m-%d').strftime("%m/%d/%Y")
        #Need to mask the SSN
        maskSSN = "***-**-"+self.SSN[-4:]
        #The format for displaying the employee
        #214,Sarah,Simpson,12/04/1985,***-**-8166,FL
        return self.EmployeeId + "," + self.FirstName + "," + self.LastName + "," + formatDate + "," + maskSSN + "," + self.State

    