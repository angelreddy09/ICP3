# 1. Create a class Employee and then do the following
# • Create a data member to count the number of Employees
# • Create a constructor to initialize name, family, salary, department
# • Create a function to average salary
# • Create a Fulltime Employee class and it should inherit the properties of Employee class
# • Create the instances of Fulltime Employee class and Employee class and call their member functions.


#Employee class
class Employee:
    count=0 #contains the count of employees
    employees=[] #contains the list of employees 
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department
        Employee.count=Employee.count+1 # count is incremented each time the employee instance is called 
        Employee.employees.append(self) # here we are adding the employee details to list 
        

        # method to calculate the average_salary of the employees
    def average_salary(self):
        avg_salary=sum(employee.salary for employee in Employee.employees) / Employee.count
        return avg_salary
    
#FulltimeEmployee class inheriting the Employee class    
class Fulltime_Employee(Employee):
        pass
    

#creating instances for above classes 
employee1=Employee("Angel Reddy Nakkala","Nakkala",100000,"IT")
employee2=Employee("Jessica Mathews","Mathews",102000,"Marketing")
fulltime_employee1 = Fulltime_Employee("Emma Stone", "Stone", 75000, "Developer")

# Call member functions
employee_list = [employee1, employee2, fulltime_employee1]

# Calculate and print the average salary of all employees
avg_salary = Employee.average_salary(employee_list)
print("Average Salary of all employees:","$",avg_salary)

# Print the total number of employees
print("Total number of employees: ",Employee.count)