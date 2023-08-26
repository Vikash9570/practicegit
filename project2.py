class Student:
    School_name="ggps"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
    def show(self,m,n):
        self.m=m
        self.n=n
        print ((self.m+self.n)/2)

    class Laptop:
        def __init__(self,cpu,ram):
            self.cpu=cpu
            self.ram=ram

        def show(self,value):
            self.value=value
            print(self.ram,self.cpu,self.value)


s1=Student("vikash",21)
# s2=Student()
lap1=Student.Laptop("rizan",16)
lap1.show("vikash")
s1.show(18,12)
print("yes")
print("branch test")



