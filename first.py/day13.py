#function
#PRE DEFINED FUNCTION AND USER DEFINE FUNCTION

#Pre-Defined
#print() int() str() list() tuple()

#def <function_name>:
#    <operation>

#<function_name()>
def hello():  # to define a function
    print("Hello World")

hello()#To call a fucntion

def area():
    U=input("Enter the distance in metre or cm=")
    L=int(input("Enter the length = "))
    b=int(input("Enter the breadth ="))
    a=L*b
    print(a," square"+c)
area()
#Function with arguments
def area(L,b):  #l,b are arguments
    a=L*b          #local variable
    print(a)
L=int(input("Enter the length= "))
b=int(input("Enter the breadth ="))
area(L,b) #l,b are arguaments
#
L=int(input("Enter the length = "))  #global variable
b=int(input("Enter the breadth ="))   #global variable
def area():
    a=L*b            #Local variable
    print(a)
area()
#
def cal(l,b,h):
    a=l*b
    v=l*b*h
    print("area is ",a)
    print("volume is ",v)
l=int(input("enter the value L= "))
b=int(input("enter the value B= "))
h=int(input("enter the value H= "))
cal(l,b,h)
 #
def area(l,b):
    a=l*b
    print(a)
def volume(l,b,h):
    v=l*b*h
    print(v)

l=int(input("Enter L= "))
b=int(input("Enter B= "))
h=int(input("enter H= "))

area(l,b)
volume(l,b,h)
#
def language(lan="Python"): #To insert default values
    print(lan)

language("C")
language("C++")
language("Java")
language("C#")
language()