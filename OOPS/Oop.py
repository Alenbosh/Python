#PYTHON OBJECT-ORIENTED PROGRAMMING


class Employee:
    num_of_emp = 0 
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        # self.email=first + '.' + last + '@company.com'

        Employee.num_of_emp += 1
    

    def apply_raise(self):
        self.pay=int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)


    #dunder method    
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

        
    @property
    def email(self):
        return('{}.{}@gmail.com'.format(self.first,self.last))

    def fullname(self):
        return('{} {}'.format(self.first,self.last))
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first= first
        self.last = last

    

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname()) 
    
    

emp_1 = Employee('manish','rajak',50000)
emp_2 = Employee('test','user',80000)

emp_1.fullname = 'manish rajak'

emp_1.first = 'Alen'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


# print(len(emp_1))
# print('test'.__len__())


# print(emp_1)

#Employee.set_raise_amount(1.05)

"""emp_1.first = 'corey'
emp_1.last = 'schafer'
emp_1.email = 'cory@gamil.com'
emp_1.pay = 50000"""
"""
emp_str_1 = "john-doe-70000"
emp_str_2 = "steve-doe-70000"
emp_str_3 = "jane-doe-70000"


new_emp_1 = Employee.from_string(emp_str_1)
#print(emp_1.raise_amount)"""

# mgr_1 = manager('sue','smith',90000,[dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# #mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()


# print(dev_1.email) 
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
"""print(dev_2.email)"""

# print(issubclass (Developer,Employee))

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1)

#dunder methods are special methods that start and end with __ 
# they are also called magic methods
# they are used to override the default behaviour of python objects
# __str__ is used to return a string representation of the object
# __repr__ is used to return a string representation of the object that can be used to recreate the object
# __str__ is used for the end user and __repr__ is used for the developer
# __str__ is more readable and __repr__ is more unambiguous
# __str__ is used when we use print() function on the object
# __repr__ is used when we use the object in the interpreter or when we use the repr() function on the object
# __str__ is used to return a string representation of the object that is easy to read and understand
# __repr__ is used to return a string representation of the object that is unambiguous and can be used to recreate the object




#dunder add
# __add__ is used to add two objects together
# print(int.__add__(1,2)) #3
# #dunder string
# print(str.__add__('hello','world')) #helloworld