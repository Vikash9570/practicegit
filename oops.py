class student:
    school="ggps"
    def __init__(self,sub,m1,m2):
        self.sub=sub
        self.m1=m1
        self.m2=m2

    def show(self):
        print(self.sub,self.m1,self.m2)
        
    class laptop:
        def __init__(self):
            self.brand="hp"
            self.proc="i5"

        def show(self):
            print(self.brand,self.proc)
    
# lap=student.laptop()
s1=student("eng",12,14)
s2=student("math",15,18)
lap1=s1.laptop()
lap1.show()
s1.show()


