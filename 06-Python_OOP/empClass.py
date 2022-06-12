class Employee:
    no_of_employees = 0 #class varible
    raise_amount = 1.04 # class variable (4% raise)
    
    def __init__(self,first,last,pay):
        ''' this is a constrcutor where all instance variables gets initiated and we can use them in later point in class'''
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@sap.com'
        self.pay = pay

        Employee.no_of_employees += 1

    def displayFullName(self):
        ''' we can see here we are accessing the class vaibales which were initiatred in the __init__'''
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp1 = Employee('Rohith','MN',90000)
emp2 = Employee('Sachin','chandapura',60000)

print(emp1.displayFullName()) #calling class method
print(emp2.email) #calling instance variable (which are unique/different w.r.t each instances)


print(emp1.pay) #pay before raise
emp1.apply_raise() #apply 4% raise
print(emp1.pay) #pay after raise


print(f"Total number of employees : {Employee.no_of_employees}")

