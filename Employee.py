# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employees:
    def __init__(self, name, ID_Number, Department, Job_Title):
        self.name = name
        self.ID_Number = ID_Number
        self.Department = Department
        self.Job_Title = Job_Title
    def __str__(self):
        return (f'{self.name} {self.ID_Number} {self.Department} {self.Job_Title}')

susan = Employees('Susan Meyers','47899','Accounting','Vice President')
mark = Employees('Mark Jones','39119','IT','Programmer')
joy = Employees('Joy Rogers','81774','Manufacturing','Engineer')
print(joy)
print(susan)
print(mark)
