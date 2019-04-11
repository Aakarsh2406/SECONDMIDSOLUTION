class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee " ,Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name)
      print("Salary: ", self.salary)
for i in range(0,5,1):
    
    emp=Employee((input('enter the name')),int(input('Enter the salary')))
    emp.displayCount()
    emp.displayEmployee()
