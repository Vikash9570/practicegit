class Student:
    School_name="ggps"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop

    def show(self,m,n):
        return (self.m+self.n)/2

    class Laptop:

        def show(self,cpu,ram):
            print(self.ram,self.cpu)


s1=Student("vikash",21)
# s2=Student()
lap1=Student.lap()
lap1.show()
s1.Student.show("i2",12)


