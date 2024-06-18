#Object oriented programming in Python
#->It focues on making reusable codes

class Hello:
    def hello(self):
        print("Hello world")

obj=Hello()
obj.hello()  #class method
#
class Area:
    @staticmethod
    def area(l,b):
        a=l*b
        print(a)

obj=Area()
l=20
b=5
obj.area(l,b)
#
class Area:
    def area(self):
        a=l*b
        print(a)

obj=Area()
l=20
b=5
obj.area(l,b)

#Init method
class Area:
    def __init__(self,l,b): 
        self.l=l
        self.b=b

    def area(self):
        a=l*b
        print(a)
l=20
b=5
obj=Area(l,b)
obj.area()

#
class Cal:
    def __init__(self,l,b,h): 
        self.l=l
        self.b=b
        self.h=h


    def area(self):
        a=self.l*self.b
        print(a)


    def volume(self):
        v=l*b*h
        print(v)

l=20
b=5
h=2
obj=Cal(l,b,h)
obj.area()
obj.volume()


#
class Cal:
    def __init__(self): 
        self.l=int(input("eNTER l="))
        self.b=int(input("Enter b= "))
        self.h=int(input("Enter h= "))


    def area(self):
        a=self.l*self.b
        print(a)


    def volume(self):
        v=l*b*h
        print(v)

obj=Cal()
obj.area()
obj.volume()
#
class Area:
    def __init__(self,l,b): 
        self.l=l
        self.b=b
    


    def area(self):
        a=self.l*self.b
        print(a)

        
class Volume:
    def __init__(self,l,b,h): 
        self.l=l
        self.b=b
        self.h=h

    def volume(self):
        v=self.l*self.b*self.h
        print(v)

l=int(input("enter L="))
b=int(input("Enter b= "))
h=int(input("eNTER H= "))

obj.area()
obj.volume()

#
