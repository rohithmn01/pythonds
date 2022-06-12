class Employee:
    raise_amount = 1.04
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.email = fname + '.' + lname + '@sap.com'
        self.pay = pay

    def payRaise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def setPayRaise(cls,amount):
        cls.raise_amount = amount


    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


import datetime
my_date = datetime.date(2022,6,13) #year,month,date
print(my_date) #2022-06-13
print(Employee.isWorkday(my_date))


emp1 = Employee('Rohith','MN',90000)
emp2 = Employee('Sachin','CS',60000)


print(emp1.pay)
Employee.setPayRaise(1.05) 
#the above line is similar to Employee.raise_amount = 1.05
emp1.payRaise()
print(emp1.pay)