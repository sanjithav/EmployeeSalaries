"""Employee Salaries"""
# Name 1: Swati Misra
# EID 1: SM83264

# Name 2: Sanjitha Venkata
# EID 2: sv28325

class Employee:
    """Defines employee"""
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.identifier = kwargs.get("identifier", None)
        self.salary = kwargs.get("salary", 0)

    def __str__(self):
        self.salary = str(self.salary) if self.salary!=0 else "None" #how to print None
        return "Employee\n" + self.name+","+ self.identifier+","+self.salary

    # #added ternary operator to return string None if value is blank

############################################################
############################################################
############################################################
class PermanentEmployee(Employee):
    """Defines permanent employee"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiplier = 0
        self.benefits = kwargs.get("benefits", 0)

        # if self.salary is not None and self.benefits is not None:
        #     self.salary *= self.multiplier

    def cal_salary(self):
        """cal salary of permanent employee"""
        if "retirement" in self.benefits and "health_insurance" in self.benefits:
            self.multiplier = 0.7
        elif "retirement" in self.benefits:
            self.multiplier = 0.8 #cant multiply None and Float
        elif "health_insurance" in self.benefits:
            self.multiplier = 0.9
        else:
            self.multiplier=1

        return float(self.salary*self.multiplier)

    def __str__(self):
        return "PermanentEmployee\n" + self.name+","+ self.identifier+","\
            +str(self.salary)+","+ str(self.benefits)

############################################################
############################################################
############################################################
class Manager(Employee):
    """Defines manager"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus", 0)
        # if self.salary is not None and self.bonus is not None:
        #     self.salary += self.bonus

    def cal_salary(self):
        """cal salary of manager"""
        return float(self.salary +self.bonus)

    def __str__(self):
        return "Manager\n"+self.name+","+self.identifier+","+str(self.salary)+","+str(self.bonus)

############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    """Defines temp employee"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours", 0)
        # str(self.salary) if salary!=0 else "None"

    def cal_salary(self):
        """returns cal salary of temp employee"""
        return float(self.hours*self.salary)

    def __str__(self):
        return "TemporaryEmployee\n" + self.name+","+self.identifier+","+\
            str(self.salary) + ","+str(self.hours)


############################################################
############################################################
############################################################
class Consultant(TemporaryEmployee):
    """Defines consultant"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel", None)
        # if self.salary is not None:
        #     self.salary = (self.salary * self.hours) + (self.trips * 1000)

    def cal_salary(self):
        return float((self.salary * self.hours) + (self.travel * 1000))

    def __str__(self):
        return "Consultant\n"+self.name+","+self.identifier+","+str(self.salary)+","+\
            str(self.hours)+","+str(self.travel)


############################################################
############################################################
############################################################
class ConsultantManager(Consultant, Manager):
    """Defines consultant manager"""
    def cal_salary(self):
        return float((self.salary * self.hours) + (self.travel * 1000) + self.bonus)

    def __str__(self): ##WILDLY GUESSING HERE LOL
        return "ConsultantManager\n"+self.name+","+self.identifier+","+str(self.salary)+","+\
            str(self.hours)+","+str(self.travel)

############################################################
############################################################
############################################################

def main():
    ''' ##### DRIVER CODE #####
        ##### Do not change. '''

    # create employees
    chris = Employee(name="Chris", identifier="UT1")
    emma = PermanentEmployee(name="Emma", identifier="UT2", salary=100000, \
                             benefits=["health_insurance"])
    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    charlotte = Manager(name="Charlotte", identifier="UT5", \
                        salary=1000000, bonus=100000)
    matt = ConsultantManager(name="Matt", identifier="UT6", salary=1000, \
                             hours=40, travel=4, bonus=10000)

    # print employees
    print(chris, "\n")
    print(emma, "\n")
    print(sam, "\n")
    print(john, "\n")
    print(charlotte, "\n")
    print(matt, "\n")

    # calculate and print salaries
    print("Check Salaries")
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement","health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    print("Sam's Salary is:", sam.cal_salary())
    print("John's Salary is:", john.cal_salary())
    print("Charlotte's Salary is:", charlotte.cal_salary())
    print("Matt's Salary is:",  matt.cal_salary())

if __name__ == "__main__":
    main()
