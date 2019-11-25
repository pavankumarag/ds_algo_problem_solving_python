class Person:
    def print_name(self):
        print (self.name)
        
person = Person()
person.name = "Pavan A G"
person.print_name()

Person.print_name(person)

print Person.__dict__
print person.__dict__

person.__dict__['email'] = 'pavan@gmail.com'
print person.email

def print_email(self):
    print(self.email)
    
Person.print_email = print_email

person.print_email()
#All class data is stored as dict internally by python