class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def print_name(self):
        print("{0} {1}".format(self.first_name, self.last_name))

p = Person("Labhvam", "Sharma")
p.print_name()


class Student(Person):
    def __init__(self,fname, lname, kills):
        super().__init__(fname, lname)
        self.kills = kills

s = Student("Nitesh", "Dubey", 800)
s.print_name()
print(s.kills)

