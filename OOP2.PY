#inheritance -->Syntax
#
class Data:     #parent class
    def __init__(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        
    def data(self):
        print(self.name,self.age,self.add)

class Info(Data): #child class
    def info(self):
        print(f"Hello world I am {self.name}. I am from {self.add}.I am {self.age}")
name=input("Enter name= ")
age=int(input("Enter age= "))
add=input("Enter address= ")
obj=Info(name,age,add)
obj.info()

#

class Data:     #parent class
    def __init__(self,add):
        self.add=add
        
    def data(self):
        print(self.add)

class Info(Data): #child class
    def __init__(self, name, age,add):
        self.name=name
        self.age=age
        Data.__init__(self,add)

    def info(self):
        print(f"Hello world I am {self.name}. I am from {self.add}.I am {self.age}")


name=input("Enter name= ")
age=int(input("Enter age= "))
add=input("Enter address= ")
obj=Info(name,age,add)
obj.info()
#Multi level inheritance---->Syntax

class A:
    pass
class B(A):
    pass
class C(B):
    pass
obj=C()
#Multiple inheritance

class A:
    pass
class B:
    pass
class C(A,B):
    pass
obj=C()

#Encapsulation
class Data:     #parent class
    def __init__(self,name,age,add):
        self.name=name    #Public
        self._age=age      #protected member
        self.__add=add      #Private 
        
    def data(self):
        print(self.name,self.age,self.add)

class Info(Data): #child class
    def info(self):
        print(f"Hello world I am {self.name}. I am from {self.add}.I am {self.age}")
name=input("Enter name= ")
age=int(input("Enter age= "))
add=input("Enter address= ")
obj=Info(name,age,add)
obj.info()
print(obj.name) #here the name is public hence it can be seen outside of the class
print(obj._age)

#Str method
class info:
    def __init__(self):
        self.name="Ram"
        self.age=45
        self.add="kathmandu"
    def __str__(self):
        return self.name #in this case Ram ain't a string it a object now 

    
obj=info()
print(obj)
print(type(obj))

#To get values in string
obj.__str__()
#or
print(str(obj))
#Here string and object cannot concate. 1) print(obj+"Shyam")    is not possible directly

#Operator overloading
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)

p1=Point(2,3)
p2=Point(-1,2)
print(p1+p2)

#using it in market(buying)
class Point:
    def __init__(self,x=0):
        self.x=x
        print("This is intit ialize method  ",self.x)

        

    def __str__(self):
        print("this is str method",self.x)
        return str(self.x)
    
    def __add__(self,other):
        x=self.x+other.x
        print("this is add method")
        return Point(x)

p1=Point(1000)
p2=Point(2000)
p3=Point(3000)
print(p1+p2+p3)


#Polymorphism
#usig single method to test property of different class by calling the property name

class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("penguin can't fly")
    def swim(self):
        print("penguin can swim")
#common inerface
def flying_test(bird):
    bird.fly()
#instantiate objects
blu=Parrot()
peggy=Penguin()
#passing the object
flying_test(blu)
flying_test(peggy)



#
