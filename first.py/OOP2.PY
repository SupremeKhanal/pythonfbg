#inheritance -->Syntax


#
class Data:     #parent class
    def __init__(self,name,age,add):
        self.name=name
        self.age=age
        self.addaddKathmandu"
        
    def data(self):
        print(self.name,self.age,self.add)

class Info(Data): #child class
    def info(self):
        print(f"Hello world I am {self.name}. I am from {self.add}.I am {self.age}")
name=input("Enter name")
age=int(input("Enter age= "))
add=input("Enter address= ")

obj=Info(name,age,add)
obj.info()

#
