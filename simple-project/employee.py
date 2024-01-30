class Employee:
    def __init__(self,fname,lname,id,salary,date):
        self.Fname =fname
        self.Lname=lname
        self._Salary = salary
        self.Date= date
        self.Id = id

    @property
    def salary(self):
        return self._Salary

    @salary.setter
    def salary(self,salary):
        if salary < 3000:
            print("Invalid Salary minmum salary should be 3000")
        else:
            self._Salary = salary

    def display_information(self):
        return f'name is {self.Fname} {self.Lname} \nid is {self.Id} \nsalary is {self._Salary} \nstart work at {self.Date}'







E1 = Employee('mohamed','hassan',12099,2000,'7/11/200')
print(E1.display_information())

E1.salary(2000)
print(E1.display_information())

