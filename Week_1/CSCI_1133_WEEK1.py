#hello world 


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        print('{} {}'.format(self.first,self.last))

    
        

emp_1 = Employee('Daniel', 'Ravin', 6000,)
print(emp_1.full_name())
